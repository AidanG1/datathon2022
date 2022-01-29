<script>
	import Chart from 'svelte-frappe-charts';
	import { DatePicker, Loading, TimePicker, Button, Label } from 'attractions';
	import PolarChart from './PolarChart.svelte';
	import WindPrediction from './WindPrediction.svelte';
	import TFPrediction from './TFPrediction.svelte';
	let chartRef;
	let json_data = [];
	let full_labels = [];
	let full_values = [];
	let start_date = new Date(Date.now() - 86400000 * 3); // 3 days ago
	let start_time = new Date();
	let end_time = new Date();
	let end_date = new Date();
	const stations = ['KMIS', 'KBQX', 'PORO3', 'PEGF1', 'AAMC1', 'PXOC1', 'VTBT2'];
	let station = 'KMIS';
	let labels = ['Hi'];
	let values = [34];
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
	function data_change(json_data) {
		change_labels_values(start_date, end_date, start_time, end_time);
	}
	$: data_change(json_data);
	$: change_labels_values(start_date, end_date, start_time, end_time);

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

<div id="content">
	<a href="https://github.com/AidanG1/datathon2022" target="_blank">
		<img
			src="https://cdn-icons-png.flaticon.com/512/25/25231.png"
			width="50"
			alt="Github logo"
			height="50"
		/>
	</a>
</div>
<div class="grid">
	<div>
		<div>
			<img src="/logo.png" width="100" alt="Logo" />
			<h1>Breezee</h1>
			<h2>Any way the wind blows</h2>
		</div>
		<div>
			<Label for="start_date">Start Date</Label>
			<DatePicker format="%m/%d/%Y" closeOnSelection bind:value={start_date} id="start_date" />
			<TimePicker hideNow bind:value={start_time} />
		</div>
		<div>
			<Label for="end_date">End Date</Label>
			<DatePicker format="%m/%d/%Y" closeOnSelection bind:value={end_date} id="end_date" />
			<TimePicker hideNow bind:value={end_time} />
		</div>
		<Label for="station_input">Station: {station}</Label>
		<div id="buttons">
			{#each stations as button_station}
				<Button
					outline
					on:click={() => {
						station = button_station;
					}}
				>
					{button_station}
				</Button>
			{/each}
		</div>
	</div>
	<div class="span-col-3">
		<div>
			<PolarChart {station} polar_date={start_date} />
		</div>
		<div class="span-col-2">
			<WindPrediction {station} />
		</div>
	</div>
	<div class="span-col-4">
		{#await fetch_data(`https://dtbe.deta.dev/s/${station}`)}
			<h1>Loading <Loading /></h1>
		{:then}
			<Chart
				{data}
				type="line"
				bind:this={chartRef}
				title="Wind Speed"
				axisOptions={{ xIsSeries: true }}
			/>
		{/await}
		<TFPrediction {station} />
	</div>
</div>

<style>
	#content {
		position: absolute;
		top: 0px;
		right: 0px;
	}
	.grid {
		display: grid;
		grid-template-columns: repeat(4, 1fr);
		grid-gap: 10px;
	}
	.span-col-4 {
		grid-column: span 4 / auto;
	}

	.span-col-3 {
		grid-column: span 3 / auto;
	}
	.span-col-2 {
		grid-column: span 2 / auto;
	}

	img {
		display: inline-block;
	}
	:global(body) {
		background-color: beige;
	}
</style>
