---
title: Mountain Summits using Strava API & turf.js
description: Using the Strava API to figure out how often I've climbed a mountain.
---

One of my standard routes for trail running and hiking passes [a small local peak](https://en.wikipedia.org/wiki/Brocken). I've climbed the peak probably dozens of times but I wanted to find out the exact number.

I log my activities to Strava, so that's what we're working with. I have about 800 activities in there, too many to analyze by hand but a great way to get to know the [Strava API](https://developers.strava.com/).

The question then is: Given a bunch of GPS routes and a polygon marking the peak, how many of those routes include the peak?

{% include figure.html src="/assets/2019-06-19-main.jpg" alt="A route passing the summit" caption="A route (in blue) passing the peak (in red)" %}

<!--more-->

## Implementation

To answer that questions, I implemented a simple algorithm using [`turf.js`](https://github.com/Turfjs/turf), an excellent spatial analysis tool. I discuss the algorithm in detail below.

The input is a bunch of GPS routes in GeoJSON format. For that, I wrote a script to batch download all my activities from the Strava API and convert them to GeoJSON. With so many activities, I ran into rate-limiting and had to space out my requests.

[The source code is on GitHub](https://github.com/arthurhammer/brocken).

## Results

Here is what the script outputs:

	Activities: 777
	Activities with summits: 57
	Total summits: 60

	Trail running: 48, Hiking: 9
	Shortest: 8 km, longest: 59 km, mean: 21 km
	Elevation gain lowest: 363 m, highest: 1881 m, mean: 719 m

The answer is: 60 summits! 

3 activities had multiple summits, so in total 57 activities.

Finally, I combined all identified activities into a single GeoJSON and overlaid them on a map:

{% include figure.html src="/assets/2019-06-19-all.jpg" alt="All 57 routes overlaid on a map" %}


## Algorithm

First, some terminology: A *route* is a polyline of geographical coordinates. A *peak* is a circular polygon. To account for inaccuracies in the GPS data, I chose a radius of 350 m.

What is a *summit* then? Any intersection between route and peak? Almost but not quite. There are a couple of additional cases to consider.

### Split Routes

One such case is a route that *begins* within the peak. It should not count as a summit. Otherwise, we'd risk overcounting. For example, I would run up the mountain, take a lunch break, and descend later—logging both as separate routes. We don't want those to count as two summits.

### Multi-Summits

A different case is multiple summits *within a single route*. During ultra marathon training, I need to log as much elevation gain as I can. Sometimes, I run up the same peak multiple times in a single session. This time, we want those summits to be counted individually.

But what is a valid subsequent summit? Going down a few metres from the peak and right back up is probably not enough. There should be some distance in-between. 

For that, I introduced a second, larger polygon around the peak. I chose a radius of 3 km. Its boundary must be crossed between one successful summit and the next. 

{% include figure.html src="/assets/2019-06-19-multi.jpg" alt="Multiple summits within a single route" caption="Multiple summits within a single route. Right: Between the two summits, the activity crosses over the required distance away from the peak, marked by the outer circle." %}

### Finding Summits

Given these criteria, we can define our algorithm.

Let's take a closer look at the individual route segments. We obtain them by splitting the route along the summit polygon. In the example below, we arrive at seven segments:

{% include figure.html src="/assets/2019-06-19-schematic.jpg" alt="Schematic view of an activity"  %}

There are four types of segments: *Start*, *Inner*, *Loop*, *End*.

To find summits, we are only interested in two of them:

***Start***: Its end point lies on the peak's boundary. The rest lies outside the peak. A start segment always identifies one summit. 

***Loop***: Both start and end point lie on the peak boundary. The rest lies outside the peak. A loop segment identifies a summit if it is not fully contained by the outer polygon. 

As such, the example contains two successful summits.

We repeat this process for every activity and sum up the results to arrive at the total number of summits.
