<script>
	import Chart from 'svelte-frappe-charts';
	let labels = [];
	let values = [];
	let data = {
		labels: labels,
		datasets: [
			{
				values: values
			}
		]
	};
	async function fetch_data(url) {
		let response = await fetch(url);

		if (response.ok) {
			let json = await response.json();
			console.log(json.data)
			for (let point of json.data) {
				labels.push(point['datetime'])
				values.push(point['wspd'])
			}
			return json;
		} else {
			alert('HTTP-Error: ' + response.status);
		}
	}
</script>

{#await fetch_data('https://dtbe.deta.dev/s/kbqx')}
	<h1>Loading</h1>
{:then}
	<Chart {data} type="line" />
{/await}
