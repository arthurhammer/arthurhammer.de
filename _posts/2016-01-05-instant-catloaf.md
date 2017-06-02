---
title: Instant Catloaf
description: Automating lifting my mood with IFTTT, Workflow and cats.
---

{% include figure.html src="/assets/2016-01-05-catloaf.jpg" alt="catloaf" %}

This is a silly one.

For a quick pick-me-up, I sometimes browse the [catloaf forum on reddit](https://www.reddit.com/r/Catloaf/). What is a catloaf, you ask? Well, let me tell you: It is a cat that looks like…a loaf of bread. There is just something about those goofy loafing cats that instantly lifts my spirits.

## Problem

 The problem is the catloaf forum's post volume is rather low which means I've most likely seen the most recent posts. Also, there's just the general hassle of opening the website or a client and navigating the forum. Too slow. When I'm in a slump I need loaves and I need them instantly!

## Solution

The solution is to set up an instant catloaf delivery system.

{% include figure.html src="/assets/2016-01-05-screenshot.png" alt="screenshot" caption="Catloaf delivery in action" %}

For this project, my tools of choice were [IFTTT](https://ifttt.com/) and the [iOS Workflow app](https://workflow.is/):

- [This IFTTT recipe][ifttt] grabs any new image from the catloaf forum and saves it to a specified folder in Dropbox.
- [This workflow][workflow] fetches those images from Dropbox and displays them in random order.

In the end, I just open the workflow and boom: catloaf. To make it even quicker, I usually launch the workflow from Spotlight. Open Spotlight, type “catloaf”, off they go. And since it's randomized, it never gets boring.

It's a silly workflow but it makes me happy. Why not have a little fun with automation?

## Improvements

Currently, only the images without any context are saved to Dropbox. It would be nice if I could see the title and maybe a link back to the reddit thread.

You could also modify the recipe to only add new hot or top posts instead of all new posts.

## Download

[Download the IFTTT recipe here][ifttt] and [the workflow here][workflow].

[ifttt]: https://ifttt.com/recipes/405972-instant-catloaf-delivery
[workflow]: https://workflow.is/workflows/bfd6dbf05607407091d9c4f6e3fd754e
