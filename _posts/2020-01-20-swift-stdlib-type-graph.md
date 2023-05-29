---
title: Swift Standard Library Type Graph
description: Visualizing Swift standard library types and their relationships.
---

{% include figure.html src="/assets/2020-01-20-swift-stdlib-type-graph.svg" caption="Type graph of the Swift standard library" alt="Type graph of the Swift standard library" %}

Quick weekend hack: A type graph of the Swift (4.2) standard library, containing every single type and how they connect to other types.

I had this idea when browsing Apple's Swift documentation: At the bottom of the page for a given type, there's a *Relationships* section. It lists which types the current one *conforms to*, *inherits from*, or *is being conformed to*.

<!--more-->

While interesting, it can be hard to discover type relationships this way. See [`Collection`](https://developer.apple.com/documentation/swift/collection#relationships) for an example. I wanted to see a bigger picture. What kind of relationships would emerge if we were to combine all those connections into a single graph? 

{% include figure.html src="/assets/2020-01-20-swift-stdlib-type-graph2.png" caption="Some of the relationships of Collection" alt="Some of the relationships of Collection" %}

## Type Graph

You can see the resulting type grap above. Click for full size.

Looking at it, we see an abundance of protocols and structs. Swift has always been described as [protocol-oriented](https://developer.apple.com/videos/play/wwdc2015/408/) (most famously in the Crusty talk at WWDC 2015) and the graph supports that notion.

Surprisingly, there are only 6 classes in the entire standard library, everything else are value-types. For comparison, I generated a graph for the Foundation framework and it's the complete opposite there. Everything is a class.

There are a handful of clusters around protocols. Most obvious for base types like `Sequence`/`Collection` and `Equatable`/`Hashable`. But there are also notable clusters for Swift's String and numeric types.

The graph also shows the relative complexity of the numeric types: 

- `Int64` → `SignedInteger` →  `SignedNumeric` → `Numeric` 
- `Int64` → `FixedWidthInteger` →  `BinaryInteger` → `Numeric`

If you haven't worked with integers in detail, you probably have never looked at these protocols in detail. There are many such barely visible protocols in the standard library.

It'd be interesting to see how the graph evolves with future Swift versions.

## How I Made It

I created a script to create the type graph for any Swift version. [Check it out on GitHub](https://github.com/arthurhammer/swift-stdlib-vis) alongside detailed instructions.

The data is generated directly from the Swift [standard library source code](https://github.com/apple/swift/tree/main/stdlib/public/core). Before it can be used, the Swift source code needs preprocessing with the [`gyb`](https://github.com/apple/swift/blob/main/utils/gyb.py) preprocessor. I parsed the generated code with [sourcekitten](https://github.com/jpsim/SourceKitten), a fantastic command-line tool to call into SourceKit. From there, I extract all public Swift types and create the type relationship graph. The graph is then rendered into a PDF/SVG with graphviz.
