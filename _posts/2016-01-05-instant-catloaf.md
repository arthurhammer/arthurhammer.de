---
title: Instant Catloaf
description: Automating lifting my mood with IFTTT, Workflow and cats.
---

{% include figure.html src="/assets/2016-01-05-catloaf.jpg" alt="catloaf" %}

For a quick pick-me-up, I sometimes browse the [catloaf forum](https://www.reddit.com/r/Catloaf/). At catloaf is a cat that looks like...a loaf. There is just something special about those goofy cats.

<!--more-->

The problem is the catloaf forum's post volume is rather low which means I've most likely seen the most recent posts. Also, there's just the general hassle of opening the website and navigating the forum. Too slow. I wanted to speed up my catloaf delivery for when I need it the most.

## Solution

My solution was to set up an instant catloaf delivery system. It comes in two parts:

- [This IFTTT recipe][ifttt] grabs any new image from the forum and saves it to a folder in Dropbox.
- [This iOS Workflow][workflow] fetches those images and displays them in random order.

In the end, I just open the workflow and boom, a random bunch of loaves. It's silly but it works.

{% include figure.html src="/assets/2016-01-05-screenshot.png" alt="screenshot" caption="Catloaf delivery in action." %}

## Improvements

Currently, only the images without any context are saved to Dropbox. It would be nice if I could see the title and maybe a link back to the forum thread.

To reduce the volume, you could also modify the recipe to only add new hot or top posts instead of all new posts.

## Download

[Download the IFTTT recipe here][ifttt] and [the workflow here][workflow].

[ifttt]: https://ifttt.com/recipes/405972-instant-catloaf-delivery
[workflow]: https://workflow.is/workflows/bfd6dbf05607407091d9c4f6e3fd754e
