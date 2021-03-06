---
title: Unhijacking Google Search Results
description: A userscript to disable Google Search results link indirections.
---

{% include figure.html src="/assets/2015-02-05-screenshot.png" alt="screenshot" %}

When you copy a link to a Google search result, Google hijacks it with an internal redirect link. Instead of `www.wikipedia.org`, you end up with something like `www.google.de/url?sa=t&rct=j&q…` on your clipboard. This is pretty inconvenient if you want to share or save the URL somewhere.

<!--more-->

I made [a userscript][download] that disables this so you always get the direct link to the search result.

It took a while finding the source of the redirection in Google's Javascript. The culprit is a global function `rwt`. To disable it, the userscript simply defines an empty [non-configurable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty) function with the same name `rwt`. The key is the non-configurability which makes it impossible for Google to override our empty `rwt` function.

Works like a charm.

[Download the userscript here][download]. You can install it in your browser with a userscript manager such as [Tampermonkey](https://tampermonkey.net/) or [Greasemonkey](https://addons.mozilla.org/en-US/firefox/addon/greasemonkey/).

[download]: https://github.com/arthurhammer/userscripts/tree/master/Google_UnhijackLinks
