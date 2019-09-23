---
title: Show All Hacker News Comments
description: A userscript to show the containing thread for a single comment page on Hacker News.
---

---

**Update December 2016**: This feature finally made it natively into Hacker News. This userscript is now obsolete.

---

{% include figure.html src="/assets/2016-04-07-screenshot.png" alt="screenshot" %}

[This userscript](https://github.com/arthurhammer/userscripts/tree/master/HackerNews_ShowAllComments) adds a button to a Hacker News comment site to bring you back to the full thread.

It's a head scratcher how this is not an existing feature on the site. The comment detail pages include no context as to which thread they belong to. Not even a title is included. When you land on a single comment from a Google Search, you're pretty much stranded.

The only thing way out is to repeatedly click the little *parent* button until you reach the root of the thread. The first iteration of the script did exactly that: It repeatedly scraped the preceding comment's page for the next URL. Later I learned about the [Hacker News API](https://hacker-news.firebaseio.com) but the API is limited so the process pretty much remained the same.

[You can find the userscript here](https://github.com/arthurhammer/userscripts/tree/master/HackerNews_ShowAllComments).
