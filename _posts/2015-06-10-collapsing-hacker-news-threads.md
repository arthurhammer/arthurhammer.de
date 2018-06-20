---
title: Collapsing Hacker News Threads
description: A browser extension to collapse comments on Hacker News.
---

***Update December 2016***: *I'm happy to see that this feature finally made it natively into Hacker News. This extension is now obsolete.*

{% include figure.html src="/assets/2015-06-10-screenshot.png" alt="screensot" %}

One thing I miss from [Hacker News](https://news.ycombinator.com) is the ability to collapse comment trees. Long threads can be quite hard to read and it is easy to lose your place. I got used to this feature on [reddit](https://www.reddit.com) and wanted to bring it over.

Here are a [Safari extension and a userscript](https://github.com/arthurhammer/hackernews-collapse), whichever you prefer. Both add a button to every comment, click it to hide or show child comments.

Before starting, I looked around to see if this had been done. I found [this old bookmarklet by Alexander Kirk](https://alexander.kirk.at/2010/02/16/collapsible-threads-for-hacker-news/). It had a few bugs and did not quite work as I intended. For one thing, it is a bookmarklet, so you have to manually activate it on every thread you visit. Extensions and userscripts would work automatically.

Instead of starting from scratch, I used Alexander's bookmarklet as a starting point. I still kept a lot of the old code so it may be a bit unruly.

I'm really satisfied with how this feature turned out.

[The code is on Github](https://github.com/arthurhammer/hackernews-collapse).