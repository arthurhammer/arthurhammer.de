---
title: Table of Contents for GitHub
description: A browser extension that adds a table of contents to GitHub readmes, wikis and gists.
---

{% include figure.html src="/assets/2015-11-27-screenshot.png" alt="screenshot" %}

A [readme](https://en.wikipedia.org/wiki/README) is the first thing you see when you open a repository on [GitHub](https://github.com). It tells you what a project is about, how to install and build it. For bigger projects, readmes can grow quite big and it becomes hard to quickly find what you are looking for. I often end up scrolling all over the place.

<!--more-->

Some project maintainers manually add a table of contents to their readmes but most don't. And it's not just readmes where I'd like to have a summary on GitHub. There are [wikis](https://help.github.com/articles/about-github-wikis/), [gists](https://help.github.com/articles/about-gists/) and basically any other [structured text file](https://github.com/github/markup). That's a lot of work to be doing manually.

Of course, I'm not the only one to have recognized this problem. [This issue](https://github.com/isaacs/github/issues/215) has hundreds of comments proposing various solutions for a GitHub native implementation. Most of them are variations of the same semi-automatic idea: Maintainers add a special markup inside the readme which is rendered as a table of contents.

## Table of Contents for GitHub

I made a small browser extension, creatively named [*Table of Contents for GitHub*](repo), to solve this problem for me. The extension lives insides the GitHub website and dynamically adds a table of contents whenever it detects you're visiting a readme or other supported content. It is unobtrusive and hides behind a small button. A click on an entry brings you to the corresponding section in the file.

The idea of this as a browser extension is that you don't depend on projects to manually add an outline to their repositories. It works automatically.

{% include figure.html src="/assets/2015-11-27-screenshot2.png" alt="screenshot" caption="You can read entire books with it." %}

There are a few other details. To avoid having to scroll back up to the table of contents if you want to look for something else, there is a small button on each heading that brings you right to it. You can also use the extension to create and edit files, wikis and gists right in the browser. It updates as you make changes.

I'm really happy with how it turned out. It's simple, unobtrusive and effective. For my needs, the extension completely resolves the issue of finding information in readmes. So far it has been received well. I have had several users write in saying they enjoy it.

## Get the Extension

Table of Contents for GitHub is available for most browsers:

- [Google Chrome][chrome] (Chrome Web Store)
- [Firefox][firefox] (Mozilla Add-ons)
- [Safari][safari]
- [Userscript][userscript]

[The code is on GitHub][repo]. Feedback and contributions welcome.

[repo]: https://github.com/arthurhammer/github-toc
[chrome]: https://chrome.google.com/webstore/detail/table-of-contents-for-git/hlkhpeomjgelmljaknhoboeohhgmmgcn
[firefox]: https://addons.mozilla.org/en-US/firefox/addon/github-toc/
[safari]: https://github.com/arthurhammer/github-toc/releases/download/v0.2.3/safari.safariextz
[userscript]: https://github.com/arthurhammer/github-toc/raw/master/dist/github-toc.user.js
