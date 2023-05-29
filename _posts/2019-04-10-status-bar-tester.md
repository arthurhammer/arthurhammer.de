---
title: Status Bar Testing during iOS Development
description: A tiny dev app for testing.
---

When the status bar on iOS changes its size, apps need to react and adapt their layout. 

 <!--more-->

{% include figure.html src="/assets/2019-04-10-statusbars.png" caption="How the in-call status bar affects app layout." %}

Auto Layout handles most things automatically. But there are cases where responding to the status bar is not trivial and requires some testing.

The Xcode Simulator has a feature to toggle the in-call status bar for testing. On a real device, it's not as easy. I've been using Maps to start GPS navigation to toggle the location status bar. This process is cumbersome and slow.

So, I made a tiny dev app for that. It has two buttons: One to choose the type of background activity (audio or location) and one to start and stop. It makes iterating on layout issues super quick.

[Download the app on GitHub](https://github.com/arthurhammer/StatusBarTester).

{% include figure.html src="/assets/2019-04-10-screenshot.png" caption="Left: Status Bar Tester. Right: During development of an app." alt="Screenshot of Status Bar Tester." %}
