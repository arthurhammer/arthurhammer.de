---
title: Emoji Fragmentation
description: An iOS Shortcut to compare emoji across platforms.
---

*Emoji Fragmentation* describes two problems in the beloved world of emoji:

1. Different platforms (and versions of platforms) support different sets of emoji.
2. The same emoji look differently across platforms.

In the first case, an emoji you send to a friend might render as a placeholder box if it's not available on her platform. In the second case, the meaning of what you wanted to say [might change lightly or sometimes drastically](https://blog.emojipedia.org/2018-the-year-of-emoji-convergence/).

I've caught myself a couple of times checking the excellent [Emojipedia](https://emojipedia.org) before sending a sensitive message to make sure my intentions remain clear emoji-wise. This is a cumbersome process so it was time to automate it.

{% include figure.html src="/assets/2018-12-05-screenshot.jpg" caption="The shortcut in action: Variants for the Face With Monocle Emoji. Expressions differ significantly." alt="Screenshot" %}

The result is [this Shortcut](https://www.icloud.com/shortcuts/34768315bcf44c06ad91401bedc88b1e) for the iOS shortcut app. It expects a single emoji character on the clipboard and shows you how it will look across platforms. You can also trigger the shortcut from Notification Center or Siri.

Limitation: Since there is no Emojipedia API, the shortcut works by scraping the corresponding Emojipedia entry. In case the site updates its HTML structure, the shortcut will most likely break.
