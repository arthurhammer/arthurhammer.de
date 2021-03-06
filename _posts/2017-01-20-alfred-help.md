---
title: Man Page for Alfred
description: A workflow that documents your workflows.
---

**Update June 2019**: This workflow was built for Alfred 3. Alfred 4 now comes with a [native feature very similar to this](https://www.alfredapp.com/whats-new/).

[Alfred](https://alfredapp.com) is the one most indispensable app on my system. In essence, it is a file launcher similar to Apple's Spotlight but it allows you to do so much more. Its power comes from user-defined *workflows* with full scripting support that can do any number of things.

<!--more-->

The problem is it's easy to lose sight of all the workflows you have installed, what they do and how they are launched. Some are launched by shortcuts and others by keywords that need remembering. Alfred itself doesn't provide much in terms of documentation for installed workflows.

{% include figure.html src="/assets/2017-01-20-screenshot.gif" caption="The Help workflow in action." alt="Screenshot" %}

I created this [Help workflow][github] for Alfred for that purpose. It lists all installed workflows and shows all their keywords and shortcuts and what they do when you execute them. To use it, use the `help` or `helptitle` commands. If you're looking for a specific command, search by title or keyword. You can also execute it right there by hitting enter.

The best part about this workflow is that you can search and trigger workflows by their names instead of remembering arbitrary shortcuts or keywords.

[Download the workflow here](https://github.com/arthurhammer/alfred-workflows/blob/master/help/Help.alfredworkflow?raw=true). [The source code is available here][github].

[github]: https://github.com/arthurhammer/alfred-workflows/tree/master/help
