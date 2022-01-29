<script>
	import { onMount } from 'svelte';
	export let station, polar_date;
	let theta = [];
	var data = [
		{
			type: 'scatterpolar',

			name: 'radial categories',

			theta: theta,

			thetaunit: 'radians',

			fill: 'toself',

			subplot: 'polar2'
		}
	];

	var layout = {
		polar: {
			domain: {
				x: [0.54, 1],

				y: [0, 0.44]
			},

			angularaxis: {
				thetaunit: 'degrees',

				dtick: 1
			}
		}
	};
	onMount(() => {
		const fmt_polar = `${polar_date.getFullYear()}-${polar_date.getMonth()}-${polar_date.getDay()}`;
		async function fetch_data() {
			let response = await fetch(`https://dtbe.deta.dev/p/${station}/${fmt_polar}`);

			if (response.ok) {
				let json = await response.json();
				for (let point of json.data) {
					theta.push(point['WSPD']);
				}
				let polarDiv = document.getElementById('polarDiv');
				let Plot = new Plotly.newPlot(polarDiv, data, layout);
				return json.data;
			} else {
				alert('HTTP-Error: ' + response.status);
			}
		}
        fetch_data()
	});
</script>

<svelte:head>
	<script src="https://cdn.plot.ly/plotly-latest.min.js" type="text/javascript"></script>
</svelte:head>

<h3>Polar Chart</h3>
<div id="polarDiv" />
