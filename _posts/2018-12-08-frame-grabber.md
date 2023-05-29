---
title: Frame Grabber
description: Releasing my first iOS app.
---

A while ago, I published my first app on the App Store, [Frame Grabber](https://apps.apple.com/app/frame-grabber/id1434703541). It's a small iOS app that lets you export individual frames of a video as still images. Pick a video in your photo library, pick a frame and share! That's it.

<!--more-->

{% include gifv.html src="/assets/2018-12-08-screenshot.mp4" caption="Using Frame Grabber to capture Eliud Kipchoge as he sets the marathon world record in Berlin 2018." alt="Frame Grabber in action." %}

## Idea

I often save favorite moments from videos I took as pictures. They're easier to remember this way. This could be a cool moment with people, a scene from a travel video or action shots like a skating trick mid-air.

Before Frame Grabber, I took screenshots of these moments or used third-party apps. But I didn't like either. So I had to make my own app.

#### Full-Quality Frames

A screenshot simply cannot capture the full detail in HD and 4k videos. It just shows what's on-screen right now.

{% include figure.html src="/assets/2018-12-08-comparison.jpg" caption="Extracting a picture from a 4k video shot on an iPhone 8." alt="Comparison of screenshots and frames extracted with Frame Grabber." %}


#### EXIF Metadata

I want exported frames to have capture date and geolocation metadata of the source video attached. This is so I can find both in my photo library next to each other.

None of the existing apps I tried had this feature. Pictures from a two year old video would appear in my photo library as if it was taken today, losing all context.

#### UX

Competing apps were, for my taste, too hard to use or full of ads.

This is an app that you open once in a while, do your thing and be done with it. It needs to be powerful yet intuitive and easy to use to accomplish its goal.

## Making the App

I had never made an app before nor any actual iOS development experience. So this was going to be an interesting experiment. 

I wanted to learn iOS devleopment from scratch.

So I set myself one rule: 

> Learn everything from the ground up, take no shortcuts.

That meant not using any dependencies and writing every single line of code myself. I made a road map and prioritized features. I learned basics of UX design and created simple mockups and wireframes. I even learned some graphic design to be able to make an icon in Sketch. 

It was incredibly eye-opening seeing how much was involved in bringing a simple prototype to a polished app in the App Store. Writing code was just one part of all of that. I'm especially thankful for all those small but valuable insights into product-development, design, customer support and more.

In hindsight, I can recommend this approach to anyone learning iOS development. Don't just focus on code, make a product!

## Open-Sourcing

I [open-sourced the app](https://github.com/arthurhammer/FrameGrabber) to give back to the community. 

While making the app, I had trouble finding non-trivial open-source iOS apps to learn from. Many open-sourced projects were just simple toy projects. Some others were enterprise level-apps developed by entire teams. These were too advanced for me for learning the fundamentals. 

I hope the code can be of use to people in a similar position as me.

## Get the App

Try Frame Grabber [on the App Store](https://apps.apple.com/app/frame-grabber/id1434703541). 

{% include figure.html src="/assets/2018-12-08-banner.png" href="https://apps.apple.com/app/frame-grabber/id1434703541" alt="Download on the App Store." %}
