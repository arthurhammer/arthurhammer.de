---
title: I Made An App
description: I published my first iOS app on the App Store, Frame Grabber.
---

{% include gifv.html src="/assets/2018-10-05-screenshot.mp4" caption="Capturing the best moment as Eliud Kipchoge sets the marathon world record in Berlin 2018." alt="Frame Grabber in action." %}

A while ago I published my first app on the App Store, [Frame Grabber](https://apps.apple.com/app/frame-grabber/id1434703541). It's a simple iOS app that lets you export individual frames of a video as still images. Pick a video in your Photo Library, pick a frame, hit share, done.

Here are my reflections on creating it.

## Idea

You're watching that Christmas of 2010 video where grandma has that look on her face when she goes on another one of her tirades, this time about how tomatoes were vegetables and not fruits in her days. You want to distill that very moment into a picture, as one does.

You’re not going to just take a screenshot like an animal, are you? No, you're better than that. What you actually want from that picture is:

1. **Full video resolution:** A screenshot is not going to cut it, you need the best quality there is.
2. **Video metadata**: You want the picture to have the same creation date and geolocation as the video. That way, it has some context and appears where it should be: right beside the video in the Photo Library, in 2010. Say no to that image appearing today, eight years later, in your Photo Library because that screenshot or other sorry excuse of an app you used couldn’t even give you a proper creation date.

Does that ever happen to you? Because to me it does, all the time. There you go: Frame Grabber. Especially the second feature I have not seen in any other app.

## Requirements

In addition to the two core features above, I had a few more requirements. Some of them stem from frustrations I had in the apps I used before:

- Fast, light, easy to use.
- Frame-by-frame stepping to select the perfect moment.
- Zooming for making out details between successive frames.
- Finding videos inside albums.
- Ad-free, spam-free, analytics-free, bloat-free, subscription-free, in-app-purchase-free.
- Free.

This is an app that you open once in a while, do your thing and be done with it. It needs to be focused on that one task.

## Implementation

I had a prototype ready in a day. It was good enough for me but I promised myself I’d release this as my first app on the App Store.

**Lesson**: There's an enormous gap between the prototype that you use yourself to the product that you want other people to use.

A good app is made of an overwhelming amount of details that rarely anybody sees. Even after I hade the core functionality and UI implemented, there’s a never-ending list of capabilities and APIs to support. Rotation, action extensions, home screen actions, NSUserActivity, 3D Touch, Haptic Feedback, localizations, accessibility, custom animations and a ton more.

Analysis paralysis overcame me. Apple adds capabilities and APIs to iOS every single year at an incredible pace, how was I going to keep up and support everything? How do other indie developers who manage to ship non-trivial apps do it? I gained a lot of respect for them.

### Un-Requirements

If I wanted to see this thing on the App Store I had to ruthlessly cut down on what I was going to include. In the end, I created a "No-list" that guided me through the entire project:

- No iPad app.
- No or only basic landscape support.
- No support for extracting multiple frames at once.
- No support for extracting frames from Live Photos or GIFs.
- No custom slide-to-dismiss gestures.
- No other fancy APIs mentioned above.
- No localizations except English and German.
- No or basic accessibility support.

Especially the last one was a tough decision as you don't want some users to be left out. If the need arises, I can always add these later but they wouldn't make it to 1.0.

**Lesson**: Do not anticipate needs and features. Cut down, implement the simplest possible solution, iterate.

### Technical Side

Three things cost most of the time: transition animations, the time slider in the video editor and managing albums in the Photo Library.

First, the transition from a photo album to the video editor and back. This was my first time implementing a [custom view controller transition](https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/CustomizingtheTransitionAnimations.html) and it's far from trivial. Initially, I wanted to make the dismissal interactive similar to the Photos app where you slide the video away with your finger. Taking the previous lesson to heart, I cut this short and decided to make the animation non-interactive. Still, I ended up learning a ton.

Second, the slider to move through the video is a fully custom component. It has a fixed value indicator and a moving track. This makes picking out the right frame easier or so I tell myself. Looking back at it, the standard slider might have sufficed.

Third, photo album support. The good: Photos framework is an amazing framework that gives you easy access to the user's entire Photo Library. The bad: As soon as you do something with albums, you hit severe limitations. In one way or another your users will have to wait. This was especially frustrating because things that appear trivial in the Photos app are not possible with Photos framework. Don't believe me? Open Instagram and go to their album chooser, have fun waiting. If freaking Instagram can't get it right, I can't.

**Lesson**: Do not make it perfect. If you're endlessly working around things trying to get it right, at some point stop and move on.

## The Non-Programming Side

Alright, coding was mostly done. On to the remaining stuff: Localization, designing the app and UI icons, preparing screenshots, copy texts, developing a marketing strategy and starting the App Store submission process.

{% include figure.html src="/assets/2018-10-05-icon.png" alt="The app icon." %}

I dreaded making the app icon because I told myself I wasn't a designer and couldn't come up with an idea let alone execute on it. I opened up Sketch and forced myself to do something, *anything*. Wasn't even hard in the end. Honestly, if there's one thing I'm proud of in this project it's the icon. It's not even good but I did it!

I cut out marketing completely. This is a whole new world I wasn't ready to get into. It's impossible to get people to use your app without some form of marketing but that wasn't my goal. My goal was to see the app on the App Store and it be free.

You need to be careful how you communicate what the app is about—either orally to your friends or pitching it in your App Store description. It seems obvious to the creator but it usually isn't. The two most common responses: "Why would you even want to do that?" and "Why not just take a screenshot?"

**Lesson**: An app is much more than programming. If you want to make a full app from the ground app, there's a lot of skills that come together.

## Conclusion

I wanted this app for myself and I made it! I owned the process from the ground app and did every single thing myself to see what's involved.

What's left:

- Probably: Improved accessibility support.
- Probably: Ability to export multiple frames.
- Probably not: Ability to export from Live Photos and GIFs.
- Unlikely: Support for iPad.

Feedback so far has been positive. Try Frame Grabber [on the App Store](https://apps.apple.com/app/frame-grabber/id1434703541). It's also [open-source](https://github.com/arthurhammer/FrameGrabber).

{% include figure.html src="/assets/2018-10-05-banner.png" href="https://apps.apple.com/app/frame-grabber/id1434703541" alt="Download on the App Store." %}
