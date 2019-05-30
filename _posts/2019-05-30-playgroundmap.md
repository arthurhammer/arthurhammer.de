---
title: Playground Map
description: Designing a map of playgrounds.
---

My girlfriend and her inner child like visiting playgrounds. As a fun little gift, I wanted to make her a custom print map of playgrounds in our city where she can check off which ones she’s visited already.

{% include figure.html src="/assets/2019-05-30-playgroundmap.jpg" caption="" alt="Playground map of Braunschweig" %}


## Getting Data

The first step was to get the data for all playgrounds in the city. [OpenStreetMap](https://openstreetmap.org) has many of them mapped. To extract the data as JSON, we can use the powerful tool [Overpass Turbo](https://overpass-turbo.eu/). It takes a little getting used to their query syntax but once you do you‘re ready to slice off any data you want.

This is query I used for getting the public playgrounds in Braunschweig:

    [out:json][timeout:25];
    {% raw %}{{geocodeArea:Braunschweig}}->.searchArea;{% endraw %}
    (
        node["leisure"="playground"]["access"!="private"](area.searchArea);
        way["leisure"="playground"]["access"!="private"](area.searchArea);
        relation["leisure"="playground"]["access"!="private"](area.searchArea);
    );
    out body;
    >;
    out skel qt;


### Validating

{% include figure.html src="/assets/2019-05-30-overpass-turbo.jpg" caption="All playgrounds extracted from OpenStreetMap." alt="All playgrounds extracted from OpenStreetMap." %}

The result contained 360 playgrounds, too many for the map I envisioned. The printed map would get too crowdy and navigating to and marking off visited ones would be difficult. From looking at satellite imagery, I found that many locations marked as playgrounds were simple sandpits. I decided to manually cross-correlate and filter with satellite imagery and with a cute children’s map provided by the local government.

Going through every single playground in the original set was quite time-consuming and boring. I thought about automating the decision process—like only including playgrounds with a minimum size or an assigned name—but in the end the manual process guaranteed the best results.

The result were 161 playgrounds. Since I'd be showing only the districts around the city center, the final map would contain even fewer than that.


## Designing the Map

Now for the fun part, designing the map.

{% include figure.html src="/assets/2019-05-30-mapstyle.jpg" caption="A map style for playgrounds." alt="A map style for playgrounds." %}

In the spirit of playing and playgrounds, I wanted the map to be lighthearted and fun, taking cues from children's maps. The street network should appear muted but other landmark features like parks and lakes I wanted to be bold. This lets the playground locations stand out but still allows the map to be used for navigation. Finally, I highlighted the city district names to give an additional navigational context.

To style the map, I used [Mapbox Studio](https://www.mapbox.com/mapbox-studio/). I started with their new [Minimo style](https://blog.mapbox.com/minimo-data-visualization-map-f4ef21687d29) which proved a good base for my map.

{% include figure.html src="/assets/2019-05-30-mapstyle2.jpg" caption="The Minimo base style and the result." alt="The base Minimo style and the result." %}

You can try out an interactive version of the map [here](https://api.mapbox.com/styles/v1/vzqdccrcq/cjw9eyf3j02r01cpdxnu8o452.html?fresh=true&title=true&access_token=pk.eyJ1IjoidnpxZGNjcmNxIiwiYSI6ImNqMGF3anphaTAyMDQycXJyZXRpZDM4YjUifQ.LLx1Mn3DOp26nxtTeSlvRg).


## Printing

Initially, I planned to make a high-quality print and frame the map but during the process I decided against it for two reasons. One, a framed map on the wall can’t be readily used for navigating to playgrounds and crossing off visited ones. Two, frames come with an obligation to hang them up the wall. In the end, I settled on a DIN A4 printout folded into a little flyer.

I’m quite pleased with the result.

{% include figure.html src="/assets/2019-05-30-playgroundmap2.jpg" caption="" alt="Playground map of Braunschweig" %}
