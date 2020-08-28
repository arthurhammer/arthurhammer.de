---
title: The iOS 14 Photos Picker and Its Limitations
description: Evaluating PHPicker for Frame Grabber.
---

The upcoming iOS 14 brings [a new Photos picker](https://developer.apple.com/videos/play/wwdc2020/10652) that allows users to select items from their photo library and hand them over to an app. According to Apple, one major benefit of the component is increased privacy for users, strongly encouraging developers to adopt it in their apps.

I evaluated the picker for adoption in [Frame Grabber](https://github.com/arthurhammer/FrameGrabber) when iOS 14 launches. Here are my results. In short: It is too buggy to be useful at this point during the beta and I won't adopt it for the time being.

<!--more-->

Let's see why but first some background.

## Custom & System Photo Pickers

Most apps that work with photos and videos provide their own custom UI for selecting items from the user's photo library. This includes Frame Grabber. The user must explicitly grant the app access to her entire photo library before items can be displayed.

The new picker, or [PHPicker](https://developer.apple.com/documentation/photokit/phpickerviewcontroller) as Apple calls it, works differently. The host app presenting the picker only receives the items the user selected. In general, the app does not get blanket access to the entire library. As such, there is no explicit authorization the app must request from the user.

### Why This Matters

Modern photo libraries have grown to tens and hundreds of thousands of items. My own contains 27k photos and videos. There's a significant amount of information in there both in the visual image data but also [in metadata alone]({% post_url 2018-12-08-visualizing-my-photo-library %}). With access to the user's photo library, it is trivial for an app to obtain locations, movement profiles and other things. It is also [easier than ever](https://developer.apple.com/documentation/vision) to detect objects, people and faces directly on the device. All that potentially going back years and decades.

Beside the possibility of abuse, there are two general problems with the custom model. First, the user doesn't have any real control. When she wants to edit a single photo with an image editor, she is pretty much forced to grant the app complete access. It is all or nothing. Second, most users are not aware of potential consequences of allowing blanket access to their photo library. Taken together, it's an illusion of choice with nothing gained for the user.

With the system picker model, the user doesn't need to make a choice. The problems are mitigated by design. However, its use by the developer is completely voluntary.


## PHPicker in Frame Grabber

Like many apps, I implemented my own custom photo library UI in Frame Grabber. Adopting PHPicker would not be a trivial change. First, I specified the exact requirements the picker needed to fulfill for my use case.

Before going over those technical requirements, a couple of pros and cons immediately stood out to me if I were to make the switch in Frame Grabber.

### Pros

**✅ Privacy**<br>Users gain trust in my app as I don't have access to their entire photo library. There's no authorization to deal with and I can drop the onboarding screen. The user isn't confronted with a privacy policy the first time she opens the app.

**✅ Consistent UI**<br>As a system-wide component, users are familiar with the picker. It closely mimicks the native Photos app. And like Photos, the picker provides a powerful search for dates, locations, objects, people and more. Super useful but out of scope for me to re-implement in Frame Grabber.

**✅ Less code, easier maintenance**<br>I can delete several screens and a few thousand lines of non-trivial code that deal with the photo library, its authorization and its data model. And I don't have the burden to keep my custom UI up to date with future iOS releases.


### Cons

**❌ Modal only**<br>The picker can only be presented modally. It cannot be integrated inline into an app's UI. This requires a re-engineering of the app's entire flow. I also believe this would make the selection process slower as it requires one more tap to present the modal.

**❌ No customization**<br>It's take it or leave it. There are a couple of things I'd lose in adopting PHPicker. A major one is Frame Grabber's inline filter button that lets the user quickly filter her photo library by videos, Live Photos or either items.

**❌ Less control**<br>I have no control about how Apple wants the picker to behave or about changes they decide implement in the future. In addition, I'm now dependent on their bugs. Video selection is a central component in my app so I'm giving up a lot.


### Technical Evaluation

In my evaluation I identified a set of ten hard requirements the picker needs to support for me to consider switching to it. Some of these are very technical since Frame Grabber is very particular in how it works with videos and Live Photos.

Since going through all ten would be tedious, let me just discuss the three where it fell short. Note that my tests were performed on beta software (iOS 14 beta 6, Xcode beta 6).

**❌ Simply doesn't work**:<br>
When accessing selected items, I did get regular permission or "file does not exist" errors. Fortunately, [Apple is aware of this issue and working on it](https://developer.apple.com/forums/thread/652695?answerId=619139022#619139022). Still, this issue significantly hindered the entire evaluation process.

**❌ Too slow**:<br>
Returning picked items is excessively slow, in the order of several seconds for a ten-second video. And the longer the video, the longer it takes. The API is documented to make a copy of the video to a temporary location but that can't be it. I can only hope this is another bug as it makes the picker completely unusable for Frame Grabber.

**❌ No determinate iCloud download progress**<br>
There doesn't appear to be a way to show the download progress percentage. This is a required feature for Frame Grabber as the app predominantly works with videos. Downloading videos from the cloud can take a long time so there needs to concrete feedback for the user. However, I checked the Notes app which seems to use PHPicker and it does show a progress bar. So, I'm hopeful this gets added in the future.


### Not Now, Maybe Soon

So, will Frame Grabber switch to the new Photos picker? No. At least not on iOS 14 launch day. The beta implementation of PHPicker is too unstable for me to be productive with it. And there are only two weeks left until the release of iOS 14.

Once iOS 14 is out of beta and has settled down a bit, I will reevaluate. I'm optimistic the issues will be resolved in the future as Apple seems to place a lot of confidence in the component. We'll see.
