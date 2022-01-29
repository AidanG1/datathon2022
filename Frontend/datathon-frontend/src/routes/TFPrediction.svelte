<script>
	export let station;
	import { Loading } from 'attractions';
	import Chart from 'svelte-frappe-charts';
	let json_data = [];
	let labels = ['Hi'];
	let values = [34];
	let new_labels = [];
	let new_values = [];
	let data = {
		labels: labels,
		datasets: [
			{
				values: values
			}
		]
	};
	let i = 0;
	async function fetch_data(url) {
		let response = await fetch(url);

		if (response.ok) {
			let json = await response.json();
			json_data = json.data;
			new_labels = [];
			new_values = [];
			i = 0;
			for (let point of json_data) {
				new_labels.push(`${i.toString()} hours`);
				new_values.push(point);
				i += 1;
			}
			data = {
				labels: new_labels,
				datasets: [
					{
						values: new_values
					}
				]
			};
			console.log(data);
			return json_data;
		} else {
			alert('HTTP-Error: ' + response.status);
		}
	}
	let chartRef
</script>

<div class="container">
	<div class="Chart">
		{#await fetch_data(`https://dtbe.deta.dev/tf/${station}`)}
			<h1>Loading <Loading /></h1>
		{:then}
			<Chart {data} type="line" bind:this={chartRef} title="Wind Speed Prediction"
			axisOptions={{ xIsSeries: true }} />
		{/await}
	</div>
</div>
