---
title: Making Table of Contents for GitHub
description: Reflecting on the Table of Contents for GitHub browser extension.
---

{% include figure.html src="/assets/2015-11-27-screenshot.png" alt="Screenshot" %}

I thought I'd reflect a bit on making [*Table of Contents for GitHub*](https://github.com/arthurhammer/github-toc) while it's still fresh in my mind.

## About

[Table of Contents for GitHub](https://github.com/arthurhammer/github-toc) is a simple browser extension that adds a table of contents to readmes, wikis, gists and basically any other structured text file on GitHub. It helps you quickly find what you are looking for. The project is partially inspired by [this popular issue](https://github.com/isaacs/github/issues/215). Read more about it [in my earlier post]({{ site.baseurl }}{% post_url 2015-11-27-table-of-contents-for-github %}).

## Related Projects

Many solutions for generating table of contents require project maintainers to hard-code them into the source files, either manually or semi-automatically. Usually, this is done by adding special markup to the file that renders into a table of contents.

This has several drawbacks:

- **It requires work**: Markup needs to be added, configured, rendered and kept up to date with changes.
- **Almost nobody does it**: For users this means that they don't get to enjoy a table of contents for most projects.
- **File-specific**: Each file that should have a table of contents needs to be configured separately. But there are many other places on GitHub where a table would be nice, e.g. wikis, gists or any other text file.

## Requirements

This project has a different premise. Instead of putting the onus on project maintainers, it is a browser extension installed by the user. It lives inside the GitHub website and works automatically. Whenever you land on structured text such as a readme, it will show an outline.

I had a few requirements for what to build. A solution should:

- be a browser extension readily available for most browsers
- generate a table of contents automatically
- provide the table not only for readmes, but for wikis, gists and any text file
- be simple, easy to use and unobtrusive

## Implementation

I started with building the Google Chrome extension first since Chrome offers the most straightforward and best documented [extension API](https://developer.chrome.com/extensions).

Adding a Safari, Firefox and userscript versions were a bit tricky. Most of the code is shared between browsers but since each one has their own extension API there were some browser-specific parts. I had to figure out how to generate four different products from the code base.

For previous projects I've only used a little bit of vanilla JavaScript. Now it was time to look into build systems. I ended up with [gulp](http://gulpjs.com/), mainly because a [project I loosely used for guidance](https://github.com/buunguyen/octotree) did. For each browser, gulp would grab the relevant files and concatenate them into the final builds. In hindsight I realise this is better solved with proper dependency management.

As for the actual functionality: Since the extension is injected into the GitHub website, I could re-use GitHub's HTML, CSS and JavaScript components. This way, the table of contents look and behaves like a GitHub native feature.

## Limitations

Whenever GitHub's HTML/CSS changes the extension might break. This has been the case a few times already. Such is the consequence of living inside another website.

The extension only works with one content item per page. That's most pages like readmes, wikis, gists. However, I have had users requesting a table of contents to *any* structured text on GitHub including comments on issues and pull requests. There would have to be a table of contents for each comment on a page of which there can be many. This requires a bit of restructuring and at this point I'm not sure if this exceeds the scope of the project.

## Outlook

There are any number of things that can be changed and added to the project. The next thing will be a search feature to allow you to filter entries in the table. Otherwise, for me, the extension is mostly feature-complete. As I don't have too much time to dedicate to the project in the near future, I will generally keep it in maintenance mode.

## What I Learned

This was a small project but I learned a bunch:

- Learning more JavaScript
- Dipping my toes into JS tooling, specifically npm and gulp
- Building a product for different targets
- Publishing extensions to Chrome Web Store and Mozilla Add-ons
- Communicating with users and the community