---
title: Pinboard Extension
description: A Safari extension for Pinboard to bookmark the current website.
---

---

**Update September 2019**: This project is deprecated. Apple droppped any support for extensions not bundled with apps from the App Store with Safari 13 (September 2019).

---

{% include figure.html src="/assets/2015-04-06-screenshot.png" alt="screenshot" %}

I have been looking for a simple [Pinboard](https://pinboard.in) browser extension for Safari but couldn't find one that I liked. The ones I did find were a tad too clunky and complex. The ideal extension would allow me to bookmark the current website in Pinboard and nothing more. It would open the default Pinboard bookmarking form and place the current mouse selection into the description field.

[I sat down and read up on Safari Extension development](https://developer.apple.com/library/content/documentation/Tools/Conceptual/SafariExtensionGuide/Introduction/Introduction.html) and quickly put together [the extension I envisioned][source]. It's nothing more than a tiny wrapper around the [Pinboard bookmarklet](https://pinboard.in/howto/). I prefer a native browser extension over a bookmarklet so I can have big toolbar button to click on.

Drawback: Extensions are browser-specific and this one is for Safari only.

## What I Learned

Making a browser extension.

This was my first time making a browser extension, albeit a trivial one. The interesting part was understanding [the architecture of an extension and how its parts fit together](https://developer.apple.com/library/content/documentation/Tools/Conceptual/SafariExtensionGuide/ExtensionsOverview/ExtensionsOverview.html#//apple_ref/doc/uid/TP40009977-CH15-SW3). Especially the distinction between the [global HTML page and injected scripts and their communication via proxies](https://developer.apple.com/library/content/documentation/Tools/Conceptual/SafariExtensionGuide/MessagesandProxies/MessagesandProxies.html#//apple_ref/doc/uid/TP40009977-CH14-SW1) appeared a bit weird at first.

I stumbled on this when I wanted to make the feature to use the current mouse selection in the bookmarking form a user preference. Injected scripts—those parts that can read webpage content such as the mouse selection—cannot access preferences. Only the global HTML page can which in return can't see webpage content. To bring this together, the injected script needs to request the user's preferences from the global page via asynchronous messaging.

In the end, this was a simple process but it still needed to be understood first.

## Download

I've been using the extension for a while now and am really pleased with it.

[Safari extension and source code are available on GitHub][source].

[source]: https://github.com/arthurhammer/pinboard-safariextension
