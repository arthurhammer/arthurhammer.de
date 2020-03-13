---
title: Alfred File Actions++
description: Bringing Alfred's File Actions to all apps.
---

{% include figure.html src="/assets/2018-07-05-screenshot.jpg" caption="File Actions in Finder." alt="Alfred File Actions" %}

[Alfred's](https://alfredapp.com) file actions are one of my most used features of the app. They allow you to quickly perform actions on the selected file in Finder like moving, deleting, sharing. I've always wanted this feature for other apps not just for Finder.

<!--more-->

Let's say I'm in Sketch editing an image and want to email it to somebody. Currently, I'd have to find the file in Finder and then bring up the file actions for it. It would be great to have a feature to show the file action panel for the currently opened file no matter in which app I am.

{% include gifv.html src="/assets/2018-07-05-screengif.mp4" caption="File Actions in any app!" alt="Workflow in action" %}

I made [this workflow](https://github.com/arthurhammer/alfred-workflows/tree/master/file-actions) for Alfred that does just that.  Press the `⌘.` shortcut (can be configured) in any document-based app and the file action panel appears, just like in Finder. This workflow is a godsend for me as it speeds up many common file-related tasks.

[Workflow and source code are available here](https://github.com/arthurhammer/alfred-workflows/tree/master/file-actions).