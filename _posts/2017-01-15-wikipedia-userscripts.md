---
title: Wikipedia Userscripts
description: Three userscripts.
---

Let me share with you three small scripts to improve your Wikipedia reading. I created these for myself a few years ago and have enjoyed them ever since. I didn't share them back then so I guess why not do it now?

<!--more-->

These extensions are implemented as [userscripts](https://en.wikipedia.org/wiki/Userscript). To install them, you need a userscript manager for your browser. I use [Tampermonkey](https://www.tampermonkey.net/).


## Quickly Switch Languages

{% include figure.html src="/assets/2019-01-15-languages.png" caption="" alt="Quick Language Switcher Screenshot." %}

I read Wikipedia articles in English and my native German. Sometimes the English version of an article has more detail, sometimes the German one. I constantly switch between both to complement and cross-reference.

However, switching the language of the current article takes too long. The language list is buried deep in the sidebar. It's often very long and changes from article to article. Finding the language you want can take a while, if it is available at all.

I [created this userscript](https://github.com/arthurhammer/userscripts/tree/master/Wikipedia_FavoriteLanguages) that adds shortcuts to your favorite languages right above the article's title. It's super quick and I love it! Note that you can configure your favorite languages within the script.

## Ditch the Sidebar

{% include figure.html src="/assets/2019-01-15-sidebar.gif" caption="" alt="oggle Sidebar in action." %}

With the languages moved out of the sidebar, there is nothing interesting left in there. I never look at it. So let's ditch it with this [userscript](https://github.com/arthurhammer/userscripts/tree/master/Wikipedia_ToggleSidebar).

The site feels immediately calmer and easier to read, don't you agree? Don't worry, if you need the sidebar, it is not gone. You can quickly toggle it by clicking on the triangle button.

## Quiet Down Links

{% include figure.html src="/assets/2016-12-01-screenshot.png" caption="" alt="Hiding Links Screenshot." %}

Ditching the sidebar is a good start to improve reading. Let's go one step further.

Wikipedia is filled with an absurd amount of links waiting to be clicked. Sometimes, it can be hard to focus on the current article with all that clutter. [This script](https://github.com/arthurhammer/userscripts/tree/master/Wikipedia_QuietWiki) quiets down those links. They're still there and can be clicked. They just won't be highlighted in blue anymore. (Although I did include a hardcore mode to disable links entirely.)

Unlike the other two, I don't have this script enabled permanently. I only enable it when I need to focus deeply on the current article.

[I wrote about this last one previously here]({% post_url 2016-12-01-quiet-links %}).

## Summary

There you have it. Three simple changes that make a lot of difference for me when reading Wikipedia. Give them a try!

Interestingly enough, I haven't needed to modify these scripts ever since I created them a few years ago. Goes to show how stable Wikipedia's HTML/CSS is.