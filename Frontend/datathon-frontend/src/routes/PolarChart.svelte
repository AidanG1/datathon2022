<script>
	import { onMount } from 'svelte';
	export let station, polar_date;
    const fmt_polar = `${polar_date.getFullYear()}-${polar_date.getMonth()}-${polar_date.getDay()}`;
	let theta = [];
	let r = [];
	let error = '';
	var data = [
		{
			type: 'scatterpolar',

			name: 'radial categories',
			r: r,

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
	onMount(() => {
		
		async function fetch_data() {
			let response = await fetch(`https://dtbe.deta.dev/p/${station}/${fmt_polar}`);

			if (response.ok) {
				let json = await response.json();
				for (let point of json.data) {
					theta.push(point['wdir']);
					r.push(point['wspd']);
				}
				let polarDiv = document.getElementById('polarDiv');
				console.log(data);
				let Plot = new Plotly.newPlot(polarDiv, data, layout);
				return json.data;
			} else {
				error = 'No data for wind direction';
			}
		}
		fetch_data();
	});
</script>

<svelte:head>
	<script src="https://cdn.plot.ly/plotly-latest.min.js" type="text/javascript"></script>
</svelte:head>

<h3>Polar Chart</h3>
{#if error === ''}
	<div id="polarDiv" />
{:else}
	<h4>{error}</h4>
{/if}
