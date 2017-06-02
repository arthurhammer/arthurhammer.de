---
title: Table of Contents for GitHub
description: A browser extension that adds a table of contents to GitHub readmes, wikis and gists.
---

{% include figure.html src="/assets/2015-11-27-screenshot.png" alt="screenshot" %}

A [readme](https://en.wikipedia.org/wiki/README) is the first thing you see when you open a repository on [GitHub](https://github.com). It tells you all about how to install, build or troubleshoot the project. For bigger projects, readmes can grow quite big and it becomes hard quickly finding what you are looking for. I often end up scrolling all over the place.

Some project maintainers manually add a table of contents to their readmes but most don't. And these aren't just readmes where I'd like to see a content summary on GitHub. There are [wikis](https://help.github.com/articles/about-github-wikis/), [gists](https://help.github.com/articles/about-gists/) and basically any other [structured text file](https://github.com/github/markup). That's a lot of work for maintainers to keep their table of contents up to date with changes.

Of course, I'm not the only one to have recognized this problem. [This issue](https://github.com/isaacs/github/issues/215) on this very topic has hundreds of enthusiastic comments calling for various solutions for a GitHub native table of contents feature. Most of them are variations of the same semi-automatic idea: You add a special markup inside the readme which, in a separate step, is rendered to a table of contents.

I decided to be proactive and implement a solution I would like myself. Instead of putting the onus on the project maintainers to insert a table of contents into each and every file, my solution would work automatically with any readme, text file, wiki, gist and what have you. Provided you install [the small browser extension][repo] I made for you ❤️.

The extension, creatively named *Table of Contents for GitHub*, lives insides the GitHub website and dynamically adds a table of contents whenever it detects you're visiting a readme or other structured text. The table hides behind a small button so it only appears when you tell it to. A click on an individual entry brings you right to the corresponding section in the readme.

{% include figure.html src="/assets/2015-11-27-screenshot2.png" alt="screenshot" caption="You can read entire books with it." %}

There are a few other details. To avoid having to scroll back to the table of contents if you want to look for something else, I added a small button to each heading that brings you right to it. You can even use the extension to create and edit files, wikis and gists right in your browser. The table keeps updated as you make changes.

I'm really happy with how it turned out. It's simple, unobtrusive and effective. For my needs, the extension completely resolves the issue of finding information in readmes. So far it has been received well. I have had several users write in saying they enjoy it.

### Get the Extension

Table of Contents for GitHub is available for the most common browsers:

- [Google Chrome][chrome] (Chrome Web Store)
- [Firefox][firefox] (Mozilla Add-ons)
- [Safari][safari]
- [Userscript][userscript]

The project is [open source on GitHub][repo]. Contributions and feedback are very welcome.

---

***Update**: Some reflections [here]({{ site.baseurl }}{% post_url 2015-12-10-making-table-of-contents-for-github %}).*

[repo]: https://github.com/arthurhammer/github-toc
[chrome]: https://chrome.google.com/webstore/detail/table-of-contents-for-git/hlkhpeomjgelmljaknhoboeohhgmmgcn
[firefox]: https://addons.mozilla.org/en-US/firefox/addon/github-toc/
[safari]: https://github.com/arthurhammer/github-toc/releases/download/v0.2.3/safari.safariextz
[userscript]: https://github.com/arthurhammer/github-toc/raw/master/dist/github-toc.user.js
