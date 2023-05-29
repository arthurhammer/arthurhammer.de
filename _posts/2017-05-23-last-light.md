---
title: Last Light
description: An iOS Workflow for sunset and daylight left.
---

{% include figure.html src="/assets/2017-05-23-trail.jpg" alt="Dark Trails" %}

What do you do when you look for a niche app with a specific set of requirements but can’t find one that you like? You make a [Workflow](https://workflow.is).

[This workflow][workflow] does one thing: It tells you when it’s going to be dark outside today.<!--more--> By dark I don’t mean sundown, I mean dark dark or [Civil Dusk](https://en.wikipedia.org/wiki/Dusk#Technical_definitions). I wanted this for when I plan my evening activities. Mostly it’s about finding a good running or walking route for the amount of daylight left.

{% include figure.html src="/assets/2017-05-23-screenshot.png" alt="Screenshot" %}

The apps I tried missed the mark in several ways:

- **No widget**: This is a prime use case for a widget. Glance at some information and done.
- **Only sundown**: Many apps included sunset and sunrise, not many the stages of [twilight](https://en.wikipedia.org/wiki/Twilight#Civil_twilight).
- **Cluttered**: Many apps had a specific focus such as photography or fishing. As such, when they did include the time of darkness it was drowned out by other irrelevant information.

The workflow, on the other hand, does everything I need perfectly. It instantly replaced the app I previously used for this niche use case. Which really is a testament to the importance of Workflow for the iOS automation environment. Now that it's [acquired by Apple](https://www.macstories.net/news/apple-acquires-workflow/), I hope it sticks around for as long as possible.

The solar data is obtained from the [Sunrise Sunset API](http://sunrise-sunset.org/api). To speed up the result, I hard-coded the location in the workflow. Alternatively, you could let Workflow geolocate you dynamically on every request.

[Get the Last Light workflow here][workflow].

[trail]: /assets/2017-05-03-trail.jpg
[screenshot]: /assets/2017-05-03-screenshot.png
[workflow]: https://workflow.is/workflows/241abb8854374bb0b415a8b8d7e6d97c
