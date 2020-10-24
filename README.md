# F1 Predictor :checkered_flag: :sparkles:

My [HackTheMidlands 5.0](https://hackthemidlands5.devpost.com/) submission :)

## What is it?

A little Python program that will generate some F1 qualifying and race results based on historic data from the [Ergast data set](http://ergast.com/mrd/).

## How did I make it?

I used [pandas](https://pandas.pydata.org/) to generate average qualifying and race positions for each driver, and each constructor (team).

Those averages are then smashed together, weighted more towards the car than the driver - since even the best driver probably couldn't win in the worst car on the grid.

## How to try it out

`config.csv` contains the data for this year's grid, if you'd like to see that. There's also a file for 2016's grid in the `data` folder.
Alternatively, you could pick some teams and drivers using the IDs in the `data` folder, or ask the program to generate some random combinations for you.
(youtube demo coming soon...)

## Is this accurate?

Not really, it's just for fun. I definitely wouldn't use this for betting purposes, lol.
