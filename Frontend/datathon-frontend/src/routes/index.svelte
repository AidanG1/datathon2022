<script>
	import FusionCharts from 'fusioncharts';
	import Timeseries from 'fusioncharts/fusioncharts.timeseries';
	import SvelteFC, { fcRoot } from 'svelte-fusioncharts';

	fcRoot(FusionCharts, Timeseries);

	let promise,
		jsonify = (res) => res.json(),
		dataFetch = fetch(
			'https://s3.eu-central-1.amazonaws.com/fusion.store/ft/data/line-chart-with-time-axis-data.json'
		).then(jsonify);
	schema = [
		{
			name: 'Time',
			type: 'date',
			format: '%h-%d-%b-%y'
		},
		{
			name: 'Wind Speed',
			type: 'number'
		}
	];
	promise = Promise.all([dataFetch]);

	const getChartConfig = ([data, schema]) => {
		const fusionDataStore = new FusionCharts.DataStore(),
			fusionTable = fusionDataStore.createDataTable(data, schema);

		return {
			type: 'timeseries',
			width: '100%',
			height: 450,
			renderAt: 'chart-container',
			dataSource: {
				data: fusionTable,
				caption: {
					text: 'Sales Analysis'
				},
				subcaption: {
					text: 'Grocery'
				},
				yAxis: [
					{
						plot: {
							value: 'Grocery Sales Value',
							type: 'line'
						},
						format: {
							prefix: '$'
						},
						title: 'Sale Value'
					}
				]
			}
		};
	};
</script>

{#await promise}
	<p>Fetching data and schema...</p>
{:then value}
	<h1>Weather Dash</h1>
	<SvelteFC {...getChartConfig(value)} />
{:catch error}
	<p>Something went wrong: {error.message}</p>
{/await}
