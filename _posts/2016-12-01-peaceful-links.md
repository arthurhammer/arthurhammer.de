---
title: Peaceful Links
description: A CSS stylesheet to mute distracting links for focused reading.
---

{% include figure.html src="https://imgs.xkcd.com/comics/the_problem_with_wikipedia.png" alt="XKCD" %}

If you have a monkey brain like me you've probably fallen down the [Wikipedia rabbit hole](https://xkcd.com/214/) more often than you like. Sometimes I set out to research a specific topic and don't even finish reading the first paragraph before being sucked into all those links. Or I find a tutorial on Google and end up opening a new browser tab for every blog post the author has ever written.

If you are not plagued by this "problem", try not to roll your eyes too much at the rest of this post.

The obvious solution is to just not open those links. *Self-control* as they say. I'm working on that. In the meantime, it's nice having a little bit of help and I got you covered.

Here's what I came up with. A stylesheet to mute distracting links:

{% include figure.html src="/assets/2016-12-01-screenshot.png" alt="Screenshot" caption="Before and after" %}

The links are still there and you can still click them if you need to, you just can't see them.[^1] Doesn't it feel quieter?

The code:

{% highlight css %}
a,
a:visited,
a:hover {
  color: inherit !important;
  text-decoration: none !important;
}
{% endhighlight %}

If this is not enough, use hard mode and disable links completely:

{% highlight css %}
a,
a:visited,
a:hover {
  color: inherit !important;
  text-decoration: none !important;
  pointer-events: none !important;
  cursor: default !important;
}
{% endhighlight %}

Try getting distracted now.

Throw the stylesheet into your stylesheet manager and enable it when you need it on a per-site basis. You could also whitelist or blacklist specific sites for it to work automatically. I personally use it as a userscript [which you can find here](https://github.com/arthurhammer/userscripts/tree/master/PeacefulLinks).

## Summary

When I first made this stylesheet I thought it would just be a silly experiment. I actually ended up using it regurlarly and found it to be quite effective for focused reading. The interesting part is that I could still quite accurately guess which words and phrases would bear links. If I needed more information I would seek out those links on my own accord. The other irrelevant ones would be kept muted instead of being highlighted and screaming "give me your attention!" at my face.

A little bit of peace.

 [^1]: Of course, this intended to be used on blocks of text such as articles or blog posts. On other sites like web apps it looks weird.
