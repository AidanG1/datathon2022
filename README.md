# 🍃[Breezee](https://breezee.me)
> Any Way The Wind Blows

### Created by Aidan Gerber, Noah Spector, Sai Mettupalli, and Jacob Kasner

# Table of Contents 📕
1. [Objectives](README.md#Objectives)
2. [Cleaning](README.md#Cleaning)
3. [Modeling](README.md#Modeling)
4. [Techstack](README.md#Techstack)
5. [Citations](README.md#Citations)

## Objectives 🧠

Breezee seeks to establish predictions for 72 hours into the future regarding "any way the wind blows," and how fast. We leverage the National Data Buoy Center's network of sensors to obtain data from the past 45 days, then display it in our dashboard alongside the future prediction model trained using the historical data.

## Cleaning

The datasets for each individual station presented themselves as text files on the National Oceanographic and Atmospheric Association's website. We developed a pipeline to request the text file given the station name and parse it into a pandas DataFrame.

## Modeling 🏋️

In order to arrive at the Long Short Term Memory model, we first needed to attempt other options.
1. Extreme Learning Machine initially seemed promising, but the methodology focuses primarily on classification.
2. Markov Chains drew from our experience in COMP 140, yet only allowed for tracking one value across time, rather than incorporating other features.
3. Simple Linear Regression across datetime provided a decent line of best fit, but could not account for the oscillating data pattern.

Long Short Term Memory performed best.

## Techstack 💻

-Deta Hosting for Dashboard
-Amazon Web Services Image for Model Training and Predictions
-JupyterNotebooks for Data Exploration and Cleaning Methodology


## Citations 🧑‍🏫

https://www.ndbc.noaa.gov/

https://www.tensorflow.org/tutorials/structured_data/time_series
