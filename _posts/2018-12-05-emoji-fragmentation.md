---
title: Emoji Fragmentation
description: An iOS shortcut to compare emojis across platforms.
---

*Emoji Fragmentation* describes two problems in the beloved world of emoji:

1. Different platforms (and versions of platforms) support different sets of emojis.
2. The same emojis look differently across platforms.

{% include figure.html src="/assets/2018-12-05-fragmentation.jpg" caption="Drooling Face emoji. Emoji images: © Apple, Samsung, Google, Microsoft" alt="Example of emoji fragmentation with the Drooling Face emoji." %}

In the first case, an emoji you send to a friend might render as a placeholder box if it's [not available on her platform](https://blog.emojipedia.org/androids-emoji-problem/). In the second case, the meaning of what you want to convey [might change slightly or sometimes drastically](https://twitter.com/jes_chastain/status/959202943340765184). While emoji support and visual styles [seem to be converging](https://blog.emojipedia.org/2018-the-year-of-emoji-convergence/) over time across platforms, fragmentation still remains a problem.

I've been known to consult the excellent [Emojipedia](https://emojipedia.org) before sending a sensitive message to make sure my intentions remain clear emoji-wise when received on a different platform. This is a cumbersome process so it was time to automate it.

{% include figure.html src="/assets/2018-12-05-screenshot.jpg" caption="The shortcut in action for the monocle emoji. Face expressions differ significantly." alt="Screenshot" %}

The result is [this shortcut](https://www.icloud.com/shortcuts/d5213325b31848cf92617db875372240) for the iOS [Shortcuts app](https://support.apple.com/guide/shortcuts/welcome/ios). It expects a single emoji character on the clipboard and shows you how it will look across platforms. You can trigger the shortcut from the share sheet, Notification Center or Siri. That way, you don't have to leave your messaging app to compare emojis.

## Limitations

The shortcut only shows the current version of an emoji for each platform. If the receiver is on an older version, the emojis might still look different.

Since there is no Emojipedia API, the shortcut works by scraping the corresponding Emojipedia entry. In case the site updates its HTML structure, the shortcut will most likely break.

## Conclusion

Emojis are serious business. [Download the shortcut here](https://www.icloud.com/shortcuts/d5213325b31848cf92617db875372240).