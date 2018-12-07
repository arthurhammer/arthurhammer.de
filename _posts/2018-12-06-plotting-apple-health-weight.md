---
title: Plotting Weight on iOS
description: Plotting Apple Health weight samples with Shortcuts and Pythonista.
---

{% include figure.html src="/assets/2018-12-06-weight.png" caption="Generated chart with Shortcuts and Pythonista." alt="Generated weight chart" %}

Sporadically, I log my weight into Apple Health on my phone. I want to see my weight charted over time but I don't like to keep yet another app around for this purpose. This is better solved with some iOS automation and the [Shortcuts](https://support.apple.com/guide/shortcuts/welcome/ios) app.

The problem is Shortcuts itself has no capability to chart data. Enter [Pythonista](http://omz-software.com/pythonista/). Pythonista is a full-fledged Python environment on your iOS device! It even includes the [`matplotlib`](https://matplotlib.org/) library which we'll use to plot the weight samples.

Since Pythonista has no API for accessing Apple Health data, we'll use Shortcuts as a frontend. [This shortcut](https://www.icloud.com/shortcuts/a262ec12bb764dae9fab4aeb59ee2c57) collects the weight samples as CSV, then calls [this Pythonista script](/assets/2018-12-06-plotweight.py) which generates the chart and returns the image back to the calling shortcut.

{% include gifv.html src="/assets/2018-12-06-screengif.mp4" %}

The result is the chart above. The cool thing is, everything—from data collection to charting—happens right on your phone and without having to install third-party one-purpose apps.

[Download the shortcut here](https://www.icloud.com/shortcuts/a262ec12bb764dae9fab4aeb59ee2c57) and [the Python script here](/assets/2018-12-06-plotweight.py) and then install it in Pythonista.