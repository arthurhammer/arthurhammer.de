---
title: I Made An App
description: Publishing my first iOS app on the App Store.
---

A while ago, I published my first app on the App Store, [Frame Grabber](https://apps.apple.com/app/frame-grabber/id1434703541). It's a simple iOS app that lets you export individual frames of a video as still images. Pick a video in your photo library, pick a frame, hit share, done.

Here are my reflections on developing and releasing the app.

{% include gifv.html src="/assets/2018-12-08-screenshot.mp4" caption="Using Frame Grabber to capture Eliud Kipchoge as he sets the marathon world record in Berlin 2018." alt="Frame Grabber in action." %}

## Idea

Often, I want to save the best moments from a video I took as standalone pictures. This could be a cute smile, a scenic landscape, a cat flopping around, whatever.

Before Frame Grabber, I took screenshots of these moments or used third-party apps. Neither were good solutions as they lacked one or both crucial things I wanted out of these pictures: full quality and video metadata.

### Full-Quality Frames

A screenshot only gives you what you see on screen. What it doesn't give you is the frame in full video quality. Current iPhones have no problem shooting videos in 4k resolution. But a screenshot of a 4k video is limited to the size of your display, of course. In addition, the playback device might compress or otherwise distort the video before displaying it on screen.

{% include figure.html src="/assets/2018-12-08-comparison.jpg" caption="Extracting a picture from a 4k video shot on an iPhone 8." alt="Comparison of screenshots and frames extracted with Frame Grabber." %}

That's just not good enough for sharing the image on social media or archiving it to my photo library. I want the best quality there is, straight out of the video.

### Video Metadata

My main use case for exporting video frames is archiving the best moments to my photo library. When scrolling through my library, the picture should appear at the same date the video was taken. Just as if I've had taken a regular photo in that moment. In similar fashion, it should have the same geolocation as the video.

None of the existing apps I tried added metadata such as [Exif](https://en.wikipedia.org/wiki/Exif) or [TIFF](https://en.wikipedia.org/wiki/TIFF) to the exported picture. Frames from a two year old video would appear in my library today, completely out of context.

## Requirements

The main functional requirements for the app then were:

- Exporting frames at full video resolution.
- Adding video metadata to exported frames.
- Precision frame-by-frame stepping to select the perfect moment.
- Zooming for making out details between successive frames.
- Selecting videos from inside photo albums.

Non-functional requirements:

- Fast, light, easy to use.
- Ad-free, spam-free, analytics-free, bloat-free, subscription-free, in-app-purchase-free.
- Free.

This is an app that you open once in a while, do your thing and be done with it. It needs to be focused on that one task.

## Implementation

I had a prototype ready in a day. It was good enough for me but I promised myself I’d release the project as my first app on the App Store.

**Lesson**: There's an enormous gap between the prototype that you use yourself to the product that you want other people to use.

A good app is made of an overwhelming amount of details that rarely anybody sees. Even after I had the main requirements and user interface implemented, there was a never-ending list of capabilities and APIs to support: an iPad app, rotation, 3D Touch, peek & pop, action extensions, home screen actions, NSUserActivity, Haptic Feedback, localizations, accessibility, custom animations and a ton more.

Analysis paralysis overcame me. Apple adds capabilities and APIs to iOS every single year at an incredible pace, how was I going to keep up and support everything? How do other indie developers who manage to ship non-trivial apps do it? I gained a lot of respect for them.

### Un-Requiring

If I wanted to see this thing on the App Store I had to ruthlessly cut down on what I was going to include. I created a "List of Noes" that guided me through the entire project:

- No iPad app.
- No or only basic landscape support.
- No support for extracting multiple frames at once.
- No support for extracting frames from Live Photos or GIFs.
- No custom slide-to-dismiss gestures.
- No other fancy APIs mentioned above.
- No localizations except English and German.
- No or basic accessibility support.

Especially the last one was a tough decision as I hated the idea of leaving out certain users. In the end, I told myself I can always add these later if the need arises. But they wouldn't make it to version 1.0.

**Lesson**: Do not anticipate needs and features. Cut down, implement the simplest possible solution, iterate.

### Technical Side

The most time was spent on three things: transition animations, the time slider in the video editor and managing albums in the photo library.

First, the transition between photo library and video editor is custom. This was my first time implementing [custom view controller transitions](https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/CustomizingtheTransitionAnimations.html). They are far from trivial. Initially, I planned to go even further and make the dismissal transition interactive—where you slide the video away with your finger back into the library. Taking the previous lesson to heart, I decided my time was best spent elsewhere and I made the animation non-interactive.

Second, the slider to move through the video is a fully custom component. It has a fixed value indicator and a moving track. This makes picking out the right frame easier—or so I tell myself. Looking back at it, I'm not sure it was worth the effort over the [built-in slider](https://developer.apple.com/documentation/uikit/uislider).

Third, supporting photo albums the way I planned was a pain. [PhotoKit](https://developer.apple.com/documentation/photokit) is very powerful in some areas and severely lacking in others. One of these is photo albums. This was especially frustrating because things that appear trivial in the Photos app are not possible with PhotoKit. Something as basic as showing a list of albums with their thumbnail images will make users wait for several seconds. Don't believe me? Open Instagram and go to their album chooser, have fun waiting. Freaking Instagram can't get it right.

**Lesson**: Do not make it perfect. If you're endlessly working around things trying to get it right, at some point stop and move on.

## The Non-Programming Side

As coding wrapped up, I continued with the remaining tasks: the German localization, designing the app and UI icons, preparing screenshots, copy texts, developing a marketing strategy and starting the App Store submission process.

{% include figure.html src="/assets/2018-12-08-icon.png" alt="The app icon." %}

I put off making the app icon as long as possible because I told myself I wasn't a designer. I thought I couldn't come up with an idea let alone execute on it. In the end, I opened up Sketch and forced myself to create something, *anything*. Wasn't even hard. Honestly, if there's one thing I'm proud of in this project it's the icon. It's not even good but I made it!

I cut out promoting the app completely. This is a whole new world I wasn't ready to get into. I know it's impossible to get people to use your app without some form of marketing but that wasn't my goal. Since Frame Grabber was supposed to be free, I didn't have any financial incentive either. My goal was to just release the app on the App Store.

Finally, you need to be careful how you communicate what an app is about—either orally to your friends or pitching it on your App Store page. The purpose of an app seems obvious to the creator but it usually isn't. The two most common responses I get when talking about Frame Grabber are "Why would you even want to do that?" and "Why not just take a screenshot?"

**Lesson**: An app is much more than programming. If you want to make a full app from the ground app, there's a lot of skills that come together.

## Conclusion

Frame Grabber was made to fill a need I had myself. I owned the development process from the ground up and did everything myself: planning, UI/UX design, implementation, release, customer support and a ton more. I wanted to learn about every single task that is needed to release a non-trivial app on the App Store. Feedback so far has been positive.

What's left:

- Probably: Improved accessibility support.
- Probably: Ability to export multiple frames.
- Probably not: Ability to export from Live Photos and GIFs.
- Unlikely: Support for iPad.

Try Frame Grabber [on the App Store](https://apps.apple.com/app/frame-grabber/id1434703541). It's also open source, [check out the code on GitHub](https://github.com/arthurhammer/FrameGrabber).

{% include figure.html src="/assets/2018-12-08-banner.png" href="https://apps.apple.com/app/frame-grabber/id1434703541" alt="Download on the App Store." %}
