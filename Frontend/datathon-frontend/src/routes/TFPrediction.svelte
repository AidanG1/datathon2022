<script>
	export let station;
	import { Loading } from 'attractions';
	import Chart from 'svelte-frappe-charts';
	let chartRef;
	let json_data = [];
	let full_labels = [];
	let full_values = [];
	let data = {
		labels: labels,
		datasets: [
			{
				values: values
			}
		]
	};
	function change_labels_values(start_date, end_date, start_time, end_time) {
		start_date.setHours(start_time.getHours());
		start_date.setMinutes(start_time.getMinutes());
		end_date.setHours(end_time.getHours());
		end_date.setMinutes(end_time.getMinutes());
		if (start_date > end_date) {
			[start_date, end_date] = [end_date, start_date];
		}
		labels = [];
		values = [];
		for (let date_value of json_data) {
			if (
				new Date(date_value['datetime']) >= start_date &&
				new Date(date_value['datetime']) <= end_date
			) {
				labels.push(date_value['datetime']);
				values.push(date_value['wspd']);
			}
		}
		data = {
			labels: labels,
			datasets: [
				{
					values: values
				}
			]
		};
	}

	async function fetch_data(url) {
		let response = await fetch(url);

		if (response.ok) {
			let json = await response.json();
			json_data = json.data;
			for (let point of json_data) {
				full_labels.push(new Date(point['datetime']));
				full_values.push(point['wspd']);
			}
			return json_data;
		} else {
			alert('HTTP-Error: ' + response.status);
		}
	}
</script>

<div class="container">
	<div class="Chart">
		{#await fetch_data(`https://dtbe.deta.dev/pred/${station}`)}
			<h1>Loading <Loading /></h1>
		{:then}
			<Chart
				{data}
				type="line"
				bind:this={chartRef}
				title="Wind Direction Prediction"
				axisOptions={{ xIsSeries: true }}
			/>
		{/await}
	</div>
</div>
