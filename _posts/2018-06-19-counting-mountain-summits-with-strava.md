---
title: Counting Mountain Summits with Strava
description: Figuring out how often I've climbed this one mountain.
---

{% include figure.html src="/assets/2018-06-19-main.jpg" caption="Finding summits" alt="The Brocken summit" %}

There's a small mountain near me that I've probably summited dozens of times so far. I don’t keep track but I’ve always been curious about the exact number. Let’s find out.

The mountain in question is the [Brocken](https://en.wikipedia.org/wiki/Brocken), with 1141 meters the highest peak in the [Harz mountains](https://en.wikipedia.org/wiki/Harz). In this post, we’ll determine the number of times I’ve successfully climbed it by analyzing all my [Strava](https://www.strava.com) activities. To date, I have about 800 runs, hikes and other activities logged on there.

[The source code for this project is on GitHub](https://github.com/arthurhammer/brocken).

## Assumptions

### Data

An activity is represented by a polyline of geographical coordinates. The summit is represented by a polygon. In particular, we’ll use a circle with a radius of 350 metres around the peak (marked red in the images). This is large enough to account for inaccuracies in the GPS data.

### Split Activities

An activity that starts directly at the summit is not counted as a successful summit. This is in response to activities where I logged ascent and descent separately. For example, I would run up the mountain, take a lunch break at the top and hike down later. If we were to treat the two parts separately, we’d risk overcounting the number of summits.

### Multi-Summits

Multiple summits *within a single activity* are counted individually. Hey, if I put in the effort, I want to see it reflected.

We need to define some criteria for what constitutes a valid subsequent summit. Going down a few metres from the peak and right back up is probably not sufficient. To make it simple, we'll use a second circle with an arbitrary radius of 3 kilometres around the peak. The boundary of this circle must be crossed between one successful summit and the next.

{% include figure.html src="/assets/2018-06-19-multi.jpg" alt="One activity with multiple summits" caption="One activity with two summits. Right: Between the two summits, the activity reaches over the required 3 km away from the peak, marked by the outer circle." %}

## Finding Summits

The basic idea is straightforward: If an activity contains a summit, its polyline must intersect the summit polygon. However, this alone is not enough as it does not account for multiple summits within a single activity.

To do that, we need to take a closer look at the individual segments of an activity. We obtain these segments by splitting up the line along the boundary of the summit.

Consider the following activity:

{% include figure.html src="/assets/2018-06-19-schematic.jpg" alt="Schematic view of an activity" caption="A schematic view of an activity. Right: The activity split into line segments by the summit polygon." %}

The activity crosses in and out of the summit three times. Cutting the activity along the summit boundary leaves us with seven individual line segments (the three inner ones included).

Of these, we can identify four different types of segments by where they lie in relation to the summit. The two interesting ones here are:

- **Start segment**: Its end point lies on the summit's boundary. The rest lies outside the summit.
- **Loop segment**: Both its start and end points lie on the summit boundary. The rest lies outside the summit.

A start segment itself marks one successful summit. A loop segment marks a summit only if it is not completely contained by the outer boundary circle. The inner and the end segments can be disregarded.

As such, the activity above contains two successful summits.

We repeat this process for every activity and sum up the results to arrive at the total number of valid summits.

## Implementation

I implemented the algorithm using the spatial analysis package [`turf.js`](https://github.com/Turfjs/turf). To get the input data, I first wrote a script to batch download all my activities from the [Strava API](https://developers.strava.com/) and convert them to [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON).

## Results

{% include figure.html src="/assets/2018-06-19-all.jpg" alt="All identified activities with summits" caption="All 57 identified summit activities." %}

Here is what the script spit out:

	Total number of activities: 777

	Total number of summits: 60

	Activities with summits: 57 (48 runs, 9 hikes)
	   Shortest: 8 km, longest: 59 km, mean: 21 km
	   Lowest elevation gain: 363 m, highest: 1881 m, mean: 719 m

60 summits is a respectable number if I say so myself.

Only three of the activities contain multiple summits. I actually expected there to be more. This is a consequence of our choice of 3 kilometres for the outer perimeter between subsequent summits. If we reduce the required radius by just 100 metres, the number of valid summits increases to 64.

Also captured: my preference of trail running over hiking.

[The source code for this project is on GitHub](https://github.com/arthurhammer/brocken).
