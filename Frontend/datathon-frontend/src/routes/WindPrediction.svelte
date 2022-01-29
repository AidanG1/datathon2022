<script>
	export let station;
	import { Loading } from 'attractions';
	import Chart from 'svelte-frappe-charts';
	let chartRef;
	let json_data = [];
	let labels = [];
	let values = [];
	let data = {
		datasets: [
			{
				values: []
			}
		]
	};
	let i = 0;
	async function fetch_data(url) {
		let response = await fetch(url);

		if (response.ok) {
			let json = await response.json();
			json_data = json.data;
			labels = [];
			values = [];
			i = 0;
			console.log(json_data)
			for (let point of json_data) {
				labels.push(i);
				values.push(point);
				i += 1;
			}
			data = {
				datasets: [
					{
						values: values
					}
				]
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
