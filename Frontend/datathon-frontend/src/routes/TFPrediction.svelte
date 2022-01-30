<script>
	export let station;
	import { Loading } from 'attractions';
	import Chart from 'svelte-frappe-charts';
	let json_data = [];
	let labels = ['Hi'];
	let values = [34];
	let new_labels = [];
	let new_values = [];
	let values_random = [];
	let data = {
		labels: labels,
		datasets: [
			{
				values: values
			}
		]
	};
	let data_random = {
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
			var min = -2;
			var max = 2;
            let random
			// and the formula is:
			for (let point of json_data) {
				new_labels.push(`${i.toString()} hours`);
				new_values.push(point);
				random = Math.floor(Math.random() * (max - min + 1)) + min;
				values_random.push(point + random);
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
			data_random = {
				labels: new_labels,
				datasets: [
					{
						values: values_random
					}
				]
			};
			console.log(data);
			return json_data;
		} else {
			alert('HTTP-Error: ' + response.status);
		}
	}
	let chartRef, chartRef2;
</script>

<div class="container">
	<div class="Chart">
		{#await fetch_data(`https://dtbe.deta.dev/tf/${station}`)}
			<h1>Loading <Loading /></h1>
		{:then}
			<Chart
				{data}
				type="line"
				bind:this={chartRef}
				title="Wind Speed Prediction Using Tensorflow GRU"
				axisOptions={{ xIsSeries: true }}
			/>
			<Chart
				{data_random}
				type="line"
				bind:this={chartRef2}
				title="Wind Speed Prediction Using Tensorflow GRU And Randomness"
				axisOptions={{ xIsSeries: true }}
			/>
		{/await}
	</div>
</div>
