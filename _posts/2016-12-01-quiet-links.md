---
title: Quiet Links
description: A CSS stylesheet to mute distracting links for focused reading.
---

{% include figure.html src="https://imgs.xkcd.com/comics/the_problem_with_wikipedia.png" href="https://xkcd.com/214/" alt="XKCD 214" caption="<a href='https://xkcd.com/license.html'>Source: XKCD</a>" %}

[Quiet Links](https://github.com/arthurhammer/userscripts/tree/master/QuietLinks) is my answer to the [Wikipedia Rabbit Hole](https://xkcd.com/214/). It is a stylesheet to quiet down links on pages to help you focus on reading.

Look at a typical Wikipedia article:

{% include figure.html src="/assets/2016-12-01-screenshot.png" alt="Screenshot" caption="The stylesheet in action" %}

There is too much noise to stay focused. Sometimes, I can't even make it past the first paragraph before getting sucked into all those links. It's fascinating information, yes, but it is not what I am after. After applying the stylesheet, the page feels markedly calmer and easier to read.

Admittedly, getting distracted by links sounds more like a me problem and not a Wikipedia problem. In either case, the stylesheet solves it. It started out as an experiment but I was surprised how much of an effect it had on my reading. I still use it regularly.

## Installing and Using

The stylesheet is not designed to be used permanently across the web. On some pages, it may interfere with the native CSS and things can look weird. For reading individual long-form articles, especially on Wikipedia, it is perfect though. Enable and disable it on a per-site basis.

In case you do need to follow links, you still can. If you hover over the text, you’ll find that links are still discoverable and clickable. There’s also a hard mode which disables links completely.

[Here is a userscript version](https://github.com/arthurhammer/userscripts/tree/master/QuietLinks) which you can install with a userscript manager like [Greasemonkey](https://addons.mozilla.org/en-US/firefox/addon/greasemonkey/) or [Tampermonkey](https://tampermonkey.net/). Or you could throw it into a stylesheet browser extension.


## Code

The following rules cover most link styles I stumbled upon:

```css
a,
a:visited,
a:hover,
a * {
  color: inherit !important;
  text-decoration: none !important;

  border: none !important;
  background-color: inherit !important;
  background-image: none !important;
  box-shadow: none !important;

  /* Hard mode: */
  /* pointer-events: none !important;
  cursor: default !important; */
}
```