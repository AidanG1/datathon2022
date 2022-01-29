<script>
	import { onMount } from 'svelte';
	export let station, polar_date;
	const fmt_polar = `${polar_date.getFullYear()}-${polar_date.getMonth()+1}-${polar_date.getDay()}`;
	let theta = [];
	let r = [];
	let error = '';
	var data = [
		{
			type: 'scatterpolar',

			name: 'radial categories',
			r: r,
            theta: theta,
			thetaunit: 'radians',

			fill: 'toself',

			subplot: 'polar2'
		}
	];

	var layout = {
		title: `Wind Speed of ${station} on ${fmt_polar}`,
		width: 500,
		height: 350,
		polar: {
			angularaxis: {
				thetaunit: 'degrees',
				dtick: 1
			}
		}
	};
	let station_change = (station, polar_date) => {
		console.log('Not mounted');
	};
	$: station_change(station, polar_date);
	onMount(() => {
		const polarDiv = document.getElementById('polarDiv');
		async function fetch_data() {
			polarDiv.innerHTML = '';
			let response = await fetch(`https://dtbe.deta.dev/p/${station}/${fmt_polar}`);
			// theta = [];
			// r = [];
			if (response.ok) {
				let json = await response.json();
				for (let point of json.data) {
					theta.push(point['wdir']);
					r.push(point['wspd']);
				}
                layout.title = `Wind Speed of ${station} on ${fmt_polar}`,
				console.log(data);
				let Plot = new Plotly.newPlot(polarDiv, data, layout);
				return json.data;
			} else {
				error = 'No data for wind direction';
			}
		}
		station_change = (station, polar_date) => {
			fetch_data();
		};
		fetch_data();
	});
</script>

<svelte:head>
	<script src="https://cdn.plot.ly/plotly-latest.min.js" type="text/javascript"></script>
</svelte:head>

<h3>Polar Chart: {station}</h3>
<div id="polarDiv" />
{#if error != ''}
	<h4>{error}</h4>
{/if}
