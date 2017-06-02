---
title: Hacker News Full Thread
description: A userscript to show the containing thread for a single comment page on Hacker News.
---

---

***Update December 2016***: *I'm happy to see that this feature has finally been added natively to Hacker News. This userscript is now obsolete.*

---

Previously: [Fixing another Hacker News shortcoming]({{ site.baseurl }}{% post_url 2015-06-10-collapsing-hacker-news-threads %}).

## Problem

Every time I land on a single comment page deep in a [Hacker News](https://news.ycombinator.com/) thread, I wonder how to get back to the full thread. There is no way of doing that short of repeatedly clicking the *parent* link until you reach the top. Um?

Worse, comment pages contain neither thread title nor a link to the submitted article. There is no context whatsoever besides the comment itself. This is fine if you navigated to the comment from the full thread. In that case, you probably know which topic you came from on. However, I often land on a single comment from a Google search and end up being stranded.

## Solution

After being slightly annoyed by this problem one too many times, I had think something up. The solution was [a userscript](https://github.com/arthurhammer/userscripts/tree/master/HackerNews_ShowAllComments) that adds a simple *all comments* button. Click it and you're back on the full thread.

{% include figure.html src="/assets/2016-04-07-screenshot.png" alt="screenshot" %}

The first iteration of the script did pretty much what I described above. It repeatedly scraped the parent page of the current comment until it reached the full thread. Only later did I learn about the [Hacker News API](https://hacker-news.firebaseio.com). But even with the API, there is no way of requesting the containing thread for a single comment. So the process remains pretty much the same.

## Download

[You can find the userscript on GitHub](https://github.com/arthurhammer/userscripts/tree/master/HackerNews_ShowAllComments).
