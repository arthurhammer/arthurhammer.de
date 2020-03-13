---
title: Status Bar Tester
description: Like ⌘Y in the Simulator but on your device.
---

{% include figure.html src="/assets/2019-09-05-statusbars.png" caption="How the in-call status bar affects the layout of your app. Left: devices without a notch. Right: with notch." alt="Types of iOS status bars." %}

When the status bar on iOS changes its size, apps need to react and adapt their layout. In theory, Auto Layout should handle most things automatically. But there are cases where responding to the status bar is not trivial and requires some testing.

 <!--more-->

The Xcode iOS Simulator contains a handy feature to toggle the in-call status bar to do just that. On a real device—which is probably where most of your testing happens—there is no such feature. Until now, I've resorted to using apps like Maps. By starting navigation and leaving it in the background the location status bar appears. This process is cumbersome and slow, especially when doing it repeatedly.

For a side project I'm developing right now, there's an issue during the presentation of a view controller I can't seem to figure out. It seems to be a UIKit bug but it leaves me going back and forth: making changes in Xcode, running the app, toggling the status bar, throwing myself on the floor crying because it doesn't work, repeat.

{% include figure.html src="/assets/2019-09-05-screenshot.png" caption="Using Status Bar Tester (left) while developing an app (right)." alt="Screenshot of Status Bar Tester." %}

Since I was tired of bothering poor Maps with this task, I made the tiny app [Status Bar Tester](https://github.com/arthurhammer/StatusBarTester) instead. It has two buttons: One to choose the type of background activity and respective status bar. And one to start the activity. It's a breeze. Deploy it to your device and get to testing.

[Download Status Bar Tester on GitHub](https://github.com/arthurhammer/StatusBarTester).