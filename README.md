# 🍃[Breezee](https://breezee.me)
> Any Way The Wind Blows

### Created by Aidan Gerber, Noah Spector, Sai Mettupalli, and Jacob Kasner

# Table of Contents 📕
1. [Objectives](README.md#objectives-)
2. [Cleaning](README.md#cleaning-)
3. [Modeling](README.md#modeling-%EF%B8%8F)
4. [Live Hosting](README.md#live-hosting-)
5. [Citations](README.md#citations-)

## Objectives 🧠

Breezee seeks to establish predictions for 72 hours into the future regarding "any way the wind blows," and how fast. We leverage the National Data Buoy Center's network of sensors to obtain data from the past 45 days, then display it in our dashboard alongside the future prediction model trained using the historical data.

## Cleaning 🧼

The datasets for each individual station presented themselves as text files on the National Oceanographic and Atmospheric Association's website. We developed a pipeline to request the text file given the station name and parse it into a pandas DataFrame.

## Modeling 🏋️

We split the wind speed and wind direction predictions into two separate models.

For wind speed, in order to arrive at the Gated Recurrent Unit model, we first needed to attempt other options.
1. Extreme Learning Machine initially seemed promising, but the methodology focuses primarily on classification.
2. Markov Chains drew from our experience in COMP 140, yet only allowed for tracking one value across time, rather than incorporating other features.
3. Simple Linear Regression across datetime provided a decent line of best fit, but could not account for the oscillating data pattern.
4. Long Short-term Memory showed promise, but it had difficulty making any predictions besides the average.

Gated Recurrent Units performed best.

For wind direction, we repurposed our already-written Markov chain to give a prediction of 8 possible directions.

## Live Hosting 💻

* Deta Deployment for Dashboard
* Amazon Web Services Image for Model Training and Predictions
* JupyterNotebooks for Data Exploration and Cleaning Methodology
* Gets data live from buoys and makes new predictions


## Citations 🧑‍🏫

https://www.ndbc.noaa.gov/

https://www.tensorflow.org/tutorials/structured_data/time_series
