---
title: Making Table of Contents for GitHub
description: Reflecting on the Table of Contents for GitHub browser extension.
---

{% include figure.html src="/assets/2015-11-27-screenshot.png" alt="Screenshot" %}

Even though it was a tiny project, I thought I'd take the time to reflect a bit on making [*Table of Contents for GitHub*](https://github.com/arthurhammer/github-toc) while it's still fresh in my mind. I've got to use this blog for something right?

## What and Why

In short, I made a browser extension that adds a table of contents to GitHub readmes, wikis, gists and basically any other structured text file on GitHub. As readmes and documentation grow bigger it is supposed to help you quickly find the information you are looking for. I found myself skimming and scrolling all over readmes and wikis when I decided I want this to happen.

You can read more about it in [this previous post]({{ site.baseurl }}{% post_url 2015-11-27-table-of-contents-for-github %}).

## Related Projects

Of course, there's already some stuff out there.

Most related projects solve the "[GitHub table of contents problem](https://github.com/isaacs/github/issues/215)" by requiring project maintainers to hard-code tables of contents right into the source files, either manually or semi-automatically. Usually this is done by adding special markup to the file that, in a separate step, is rendered into a table of contents.

This has several drawbacks:

- **It requires work**: from project maintainers.
- **It is not automatic**: It requires a separate step to build the table of contents. And it needs to be kept up to date with changes.
- **Nobody does it**: Well, almost. For you as a user this means that you don't get to enjoy a table of contents for the vast majority of projects.
- **Individual files only**: Each file that should have a table of contents needs to be marked as such. But there are many other places on GitHub where a table would be desirable, such as wikis, gists and basically any other text file.

This project has a different premise: Instead of putting the onus on project maintainers, it's a browser extension that is installed by the user. It lives inside the GitHub website and is fully automatic. Whenever you land on structured text such as a readme, boom there's your table of contents.

## Requirements

I had a few requirements for what to build. A solution should:

- be a browser extension.
- generate a table of contents fully automatically and require no work.
- provide the table not only for readmes, but for wikis, gists and any text file.
- be simple, easy to use and visually unobtrusive.
- be readily available for most browsers.

## Implementation

I started with making a Google Chrome extension first since Chrome offers the most straightforward and best documented [extension API](https://developer.chrome.com/extensions).

Adding a Safari, Firefox and userscript versions turned out to be a bit tricky. The majority of the JavaScript was shared between the browsers but since each one has their own extension API there were some browser-specific files. I had to figure out how to generate the different browser builds from the code base.

The JavaScript tooling world is quite intimidating for beginners and for [previous]({{ site.baseurl }}{% post_url 2015-04-06-pinboard-extension %}) [projects]({{ site.baseurl }}{% post_url 2015-06-10-collapsing-hacker-news-threads %}) I've only ever needed to write vanilla JS. It was time to look into build systems. I ended up with [gulp](http://gulpjs.com/), mainly because a [project I loosely used for guidance](https://github.com/buunguyen/octotree) did. For each browser, gulp would grab the relevant files and concatenate them into the final builds.

As for the main functionality itself: Since the extension is injected into the GitHub website, I could replicate GitHub's HTML structure and have their CSS style the table of contents. In addition, their JavaScript would animate and otherwise handle the table. This way, the table of contents would look and behave like a GitHub native feature which is what I required.

## Limitations

Whenever GitHub's HTML/CSS changes we need to adapt. This is the nature of living inside the website. This has happened a few times already.

The code assumes there is only ever one table of contents on the page. Makes sense: There is only ever one readme, one text file, one wiki displayed at a time. However, I have had users requesting I add a table of contents to *any* structured text on GitHub, including comments on issues and pull requests. To do that there would have to be a table of contents for each comment on a page of which there can be many. This requires a bit of restructuring. At this point I'm not sure if this exceeds the scope of the project.

## Future

There are any number of things that can be changed and added to the project. For one, I would like a search feature that would allow you to filter the table of contents.

I also want to look into proper JavaScript module patterns so I can ditch concatenating files and let a tool automatically resolve dependencies.

Finally, I plan to rework the code so as to lift the restriction of only one table of contents per page.

In the near future though, I don't have too much time to dedicate to the project. For now, I'm pleased with it and will keep it mostly in maintenance mode.

## What I Learned

Again, this was a really small and simple project. Still, I learned a bunch:

- Diving a bit deeper into JavaScript.
- Dipping my toes into JS tooling, specifically npm and gulp.
- Building a product for different targets (browsers).
- Limiting the scope of a project.
- Publishing extensions to Chrome Web Store and Mozilla Add-ons.
- Dealing with feedback and interacting with users.

I'm actually starting to like JavaScript. It's an incredibly flexible language. The tooling world is still indimitading. Nothing comes out of the box and for each need a million different solutions have been proposed. I haven't really experienced this with other ecosystems as much. My plan is to overcome this self-imposed barrier by picking one set of tools and not letting myself be overwhelmed with alternatives.
