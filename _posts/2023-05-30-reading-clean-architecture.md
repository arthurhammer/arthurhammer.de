---
title: "Reading: Clean Architecture"
description: By Robert C. Martin.
---

At work, I have been working more on modularization and architecture topics recently. I wanted to dig deeper and picked up a copy of [Clean Architecture](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/) by Robert C. Martin. 

Let me share my unconnected thoughts after reading the book.

<!--more-->

### What is Architecture

Terminology first: 

> Architecture is the structure you give your app so you can support its use cases, its development and its maintenance. 

A good architecture leaves options open and gives you flexibility. It allows you to react to new requirements easily.

Most importantly, architecture is a team effort.

### Mobile Architecture

In the mobile development world, the term architecture is often used interchangeably with MVVM, MVP, VIP, VIPER, TCA and the like. But these discussions fall short on important aspects as they leave huge chunks of an app's architecture out.

These patterns only tell us about how to design a single scene. Maybe multiple when we add a Coordinator/Router mechanism. Still, a large part of the architecture is missing. What about the service and data layers? How do we slice our modules and how do we decide what belongs in one module vs. the other? How do we connect modules without letting the dependency graph spiral out of control? And, finally, how do we keep the code extensible and maintainable while having multiple teams working on the same app?

There are important questions to answer. Apple has never helped us here. On the other hand, the [Android documentation](https://developer.android.com/topic/architecture) is much more detailed and opinionated. It's a really good starting point. I have also found articles from larger teams insightful as they have faced similar issuess (e.g. [JustEat](https://tech.justeattakeaway.com/2019/12/18/modular-ios-architecture-just-eat/) or [New Work](https://tech.new-work.se/di-in-a-modularized-project-in-swift-339fc242b4df)). Also, connecting with others at conferences has really opened my eyes.

### Clean Architecture

This is where Clean Architecture comes in for me. It's a book full of universal principles decoupled from any specific approach. Understanding the principles helps you make your own decisions instead of relying on intuition or opinion. I can't stress this point enough.

Martin builds his concepts of architecture from the smallest part into something larger. He starts with a recap of the SOLID principles. Then, he extends those principles onto the component level which is where it gets interesting. When he arrives at the largest level—the architecture level—, I felt like I was ready to come to the same conclusions as he did.

The culmination of everything is the Clean Architecture itself: It is not a vertically layered architecture but a [circular one](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html). Dependencies point from details inward to the core of the app rather than top-down from the core to details. This means that the data layer depends on the domain layer and not vice versa, for example.

### Plugin Architecture

Another way of looking at it, is that the outer layers are plugins into the core domain of an architecture. 

I really enjoyed how Martin drives home the point that the UI, the network and the database are such plugins. Or "details" as he calls them. Your domain should not depend on these details, rather they should depend on abstractions. This is dependency inversion on the package level.

This might not be intuitive at first. Beginner programmer might think the UI and database are the most important parts of an app. I have written projects where I used Core Data *everywhere*. After all, this is what Apple recommended. Even then, I knew how restrictive it made my code.

### Third-Party Dependencies

I treat third-party dependencies as plugins as well. At work, I proposed forcing every third-party dependency through a custom wrapper module. This creates a choke point enabling us to contain the dependency. Most importantly, using the Facade pattern, we can expose only the one or two use cases we actually need giving us full control.

I have experienced first-hand how difficult it is to remove a dependency that has leaked across the code-base if left uncontained. It can halt feature development for an entire team for weeks which is irresponsible. I will never go through that again.


### Screaming Architecture

One thing I've been thinking about a lot lately is ["Screaming Architecture"](https://blog.cleancoder.com/uncle-bob/2011/09/30/Screaming-Architecture.html). Just by looking at the code's structure, it should give a sense of what the app is about. It will make it much easier to find your way around the code base. Especially when your teams are scaling up or you are onboarding and offboarding many new team mates.

At work, we use feature modules which is a great start. Just by looking at the list of modules, you get a sense of the use cases the app supports. 

It gets more interesting on a smaller level. We started splitting up services into small single-purpose use case objects. This gives us a very close mapping from the actual problem domain to code. It also makes the code base easily searchable by keyword.

For example, using interface segregation, a `ProfileService` with four methods can be split into four uses cases such as `LoadProfileUseCase`, `LikeProfileUseCase`, `SendMessageToProfileUseCase`, `ReportProfileUseCase`. 

### Scratching the Surface

At times, I wish the book would go into more detail. Many chapters are kept short, ending right when it gets interesting. For example, in chapter 28 *The Test Boundary*, Martin introduces the concept of the *Testing API*:

> The purpose of the Testing API is to decouple the tests from the application. This decoupling encompasses more than just detaching the tests from the UI: The goal is to decouple the structure of the tests from the structure of the application.

That's it. He doesn't give any other details. Why introduce the concept then at all, I'm wondering? Tightly coupled tests are a very real problem[^1] and I was left longing for more on how Martin uses this "Testing API" to solve it.

One of the most hands-on chapters was the last one, aptly named *The Missing Chapter*. It compares the various packaging strategies found in practice. A chapter packed with practical wisdom and I wish some others were as detailed as this one.

To fill the gaps and go into more details, I already picked out the next book I will be reading: *Principles of Package Design* by Matthias Noback.


### Conclusion

Such a great book condensing Martin's decades of experience. It focuses on concepts instead of techniques, making it a timeless work.

I took a lot from it. Some aspects I had applied deliberitely or intuitively before and this book was a welcome refresher. Other concepts were completely new to me. I already started applying them at work. One of the most important takeaways for me is how I can base architecture design and analysis on proven principles instead of just being guided by intuition. 


[^1]: I recommend *Unit Testing: Principles, Practices, and Patterns* by Vladimir Khorikov for more on that topic.