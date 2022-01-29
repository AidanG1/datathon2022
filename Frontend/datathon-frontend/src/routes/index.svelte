<script>
	import Chart from 'svelte-frappe-charts';
	import { DatePicker, Loading, TimePicker, Button, Label } from 'attractions';
	let chartRef;
	let json_data = [];
	let full_labels = [];
	let full_values = [];
	let start_date = new Date(Date.now() - 86400000 * 3); // 3 days ago
	let start_time = new Date();
	let end_time = new Date();
	let end_date = new Date();
	const stations = ['KBQX', 'KIKT', 'KMIS'];
	let station = 'KBQX';
	let labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
	let values = [18, 40, 30, 35, 8, 52, 17, -4];
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

<header>
	<img src="/logo.png" width="100" alt="Logo" />
</header>
<div class="controls">
	<Label for="start_date">Start Date</Label>
	<DatePicker format="%m/%d/%Y" closeOnSelection bind:value={start_date} id="start_date" />
	<TimePicker hideNow bind:value={start_time} />
	<Label for="end_date">End Date</Label>
	<DatePicker format="%m/%d/%Y" closeOnSelection bind:value={end_date} id="end_date" />
	<TimePicker hideNow bind:value={end_time} />
	<Label for="station_input">Station</Label>
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
<div class="container">
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
</div>

<style>
	img {
		display: inline-block;
	}

	:global(button) {
		display: inline-block;
	}

	:global(input) {
		display: inline-block;
	}
</style>
