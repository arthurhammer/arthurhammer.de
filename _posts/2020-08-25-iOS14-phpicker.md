---
title: PHPicker and Frame Grabber
description: Evaluating the new iOS 14 Photos picker.
---

The upcoming iOS 14 brings [a new Photos picker](https://developer.apple.com/videos/play/wwdc2020/10652) that allows users to select items from their photo library and hand them over to an app. According to Apple, one major benefit of the component is increased privacy for users, strongly encouraging developers to adopt it in their apps.

In this post, I'll walk myself through the decision process of whether or not to adopt the new picker in [Frame Grabber](https://github.com/arthurhammer/FrameGrabber). This is a bit of a dry one, you've been warned.


<!--more-->

## Custom & System Photo Pickers

Most apps that work with photos and videos provide their own custom UI for selecting items from the user's photo library. This includes Frame Grabber. The user must explicitly grant the app access to her entire photo library before items can be displayed.

The new picker, or [PHPicker](https://developer.apple.com/documentation/photokit/phpickerviewcontroller) as Apple calls it, works differently. The host app presenting the picker only receives the items the user selected. In general, the app does not get blanket access to the entire library. As such, there is no explicit authorization the app must request from the user.

### Why This Matters

Modern photo libraries have grown to tens and hundreds of thousands of items. My own contains 27k photos and videos. There's a significant amount of information in there both in the visual image data but also [in metadata alone]({% post_url 2018-12-08-visualizing-my-photo-library %}). With access to the user's photo library, it is trivial for an app to obtain locations, movement profiles and other things. It is also [easier than ever](https://developer.apple.com/documentation/vision) to detect objects, people and faces directly on the device. All that potentially going back years and decades.

Beside the possibility of abuse, there are two general problems with the custom model. First, the user doesn't have any real control. When she wants to edit a single photo with an image editor, she is pretty much forced to grant the app complete access. It is all or nothing. Second, most users are not aware of potential consequences of allowing blanket access to their photo library. Taken together, it's an illusion of choice with nothing gained for the user.

With the system picker model, the user doesn't need to make a choice. The problems are mitigated by design. However, its use by the developer is completely voluntary.


## PHPicker in Frame Grabber

Like many apps, I implemented my own custom photo library UI in Frame Grabber. Adopting PHPicker is not a trivial change. It has an entirely [different API](https://developer.apple.com/documentation/photokit/phpickerviewcontroller) and data model than [the direct photo library API](https://developer.apple.com/documentation/photokit/phasset). Videos and Live Photos are a central component of Frame Grabber, so I had to verify everything I needed was supported.

Before I going over the technical requirements, there were three high-level pros and cons each that stood out to me if I were to make the switch.

### Reasons to Switch

**✅ Privacy**<br>Users gain trust in my app as I don't have access to their entire photo library. There's no authorization to deal with and I can drop the onboarding screen. The user isn't confronted with a privacy policy the first time she opens the app.

**✅ Consistent UI**<br>As a system-wide component, users are familiar with the picker. It closely mimicks the native Photos app. And like Photos, the picker provides a powerful search for dates, locations, objects, people and more. Super useful but out of scope for me to re-implement in Frame Grabber.

**✅ Less code, easier maintenance**<br>I can delete several screens and a few thousand lines of non-trivial code that deal with the photo library, its authorization and its data model. And I don't have the burden to keep my custom UI up to date with future iOS releases.


### Reasons Not to Switch

**❌ Modal only**<br>The picker can only be presented modally. It cannot be integrated inline into an app's UI. This requires a re-engineering of the app's entire flow. I believe this would make the selection process slower as it requires one more tap to present the modal.

**❌ No customization**<br>It's take it or leave it. There are a couple of things I'd lose in adopting PHPicker. A major one is Frame Grabber's inline filter button that lets the user quickly filter her photo library by videos, Live Photos or either items.

**❌ Less control**<br>I have no control about how Apple wants the picker to behave or about changes they decide implement in the future. In addition, I'm now dependent on their bugs. Video selection is a central component in my app so I'm giving up a lot.


### Technical Requirements

1. **Filtering**: Can the picker be set to show only videos and/or Live Photos?

    ✅ **Yes**.

2. **Maintaining context**: Can the picker resume at the last place the user navigated to when presented several times (e.g. specific photo album)?

   ✅ **Yes**.

3. **iCloud loading**: Does the picker automatically download items from iCloud or provide an API to do so manually?

    ✅ **Yes**. Automatically.

4. **iCloud progress tracking**: For iCloud downloads, does the picker provide an API to track determinate progress?

    ❌ **No**. [Not supported as confirmed by an Apple engineer](https://developer.apple.com/forums/thread/652695?answerId=629922022#629922022). Apple's Notes app does seem to have this capability within PHPicker and I think it should be available to all developers. I filed an enhancement request (FB8585202).

5. **Full resolution**: Are items returned in full quality and resolution?

    ✅ **Yes**. In general, the most current version of an asset is returned.

6. **Live Photo components**: Can the photo and video components of a Live Photo be accessed separately?

    ✅ **Yes**. Live Photos are returned as `.pvt` bundles which are simple folders containing both components.

7. **Video metadata**: Do videos include metadata (like creation date, geolocation etc.)?

    ✅ **Yes**. Edge case: The metadata can divert from the one displayed in the Photos app. The [metadata in the Photos app](https://developer.apple.com/documentation/photokit/phasset) can be edited independently of the source [metadata from the video file](https://developer.apple.com/documentation/avfoundation/avasset) it was extracted from. With full photo library access, we have access to both variants. With PHPicker however, we only have access to the video file metadata. This can be a problem since, in case of doubt, the user would prefer the information displayed in the Photos app. To be fair, this is a rare case.

8. **Live Photo metadata**. Do both Live Photo components include metadata?

    ✅ **Yes**. Same considerations as above.

9.  **Edited items metadata**: Do edited items include metadata?

    ✅ **Yes**. Same considerations as above.

## Conclusion

PHPicker fulfills almost all my requirements. However, I am not switching over quite yet. There are two things that need to be resolved.

First, missing iCloud download progress tracking is a big issue. While photos load very quickly, videos might not. Videos can be arbitrarily large. Without determinate progress, the user doesn't have any indication for how long the download might take. That's not a good experience. I hope, this capability will be added in the future.

The seconds issue is the one of modal presentation. Switching from a primary-secondary interface to a modal interface requires me to re-think my entire UI. I don't have a good solution for that yet.

In the end though, it comes down to Apple's litmus test: "Does your app really *need* full photo library access? If not, then switch to PHPicker." I anticipated the answer would be "yes". But now that I have evaluated PHPicker, I come to the conclusion the answer is actually "no". From a technical standpoint, Frame Grabber does not necessarily need full access to the user's photo library. This adds a bit of external pressure to actually do go through with it.

---

This evaluation was more work than it looks. The documentation was very sparse and it took lots of trial and error. There were several hiccups and bugs on Apple's side during my tests. Luckily, most issues could be resolved after consulting with Apple engineers through the developer forums.
