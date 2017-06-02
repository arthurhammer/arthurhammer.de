---
title: Collapsing Hacker News Threads
description: A browser extension to collapse comments on Hacker News.
---

---

***Update December 2016***: *I'm happy to see that this feature has finally been added natively to Hacker News. And it pretty much works exactly like my extension. The extension is now obsolete.*

---

The [Hacker News](https://news.ycombinator.com) site is as plain as it gets. One thing that irks me is that there is no option to collapse comment trees. Long threads can be quite hard to read and it is easy to lose your place. Compare this with sites like [reddit](https://www.reddit.com) where collapsing comments is an intricate part of the comment section.

{% include figure.html src="/assets/2015-06-10-screenshot.png" alt="screensot" caption="Collapsing comments on Hacker News" %}

I implemented a [Safari extension and a userscript](https://github.com/arthurhammer/hackernews-collapse) that adds this missing functionality. There's now a collapse button on each comment header. Click it and the comments are gone.

Before getting to work, I looked around to see if this had already been done. I found an [old bookmarklet by Alexander Kirk](https://alexander.kirk.at/2010/02/16/collapsible-threads-for-hacker-news/). It had several bugs and did not quite work as I intended. For one thing, it is a bookmarklet, so you have to manually activate it on every thread you visit. Extensions and userscripts would work automatically.

Instead of starting from scratch, I decided to use Alexander's bookmarklet as a starting point. I made many changes to it and fixed several bugs. I still kept a lot of the old code so it may be a bit ugly.

I'm really satisfied with this extension. I use it to collapse comments pretty much every time I visit Hacker News.

## Download

[Download Safari extension and userscript on Github](https://github.com/ahammer-/hackernews-collapse).
