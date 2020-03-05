---
title: Fine-Scrubbing Videos with UISlider
description: A drop-in UISlider subclass that adds variable scrubbing speeds.
---

Scrubbing through a video with a slider can be difficult. The longer the video is, the less accurate the scrubbing will be. Selecting a specific moment in the video can get fiddly and frustrating.

There's a nice solution to this, rather hidden in iOS’ video player component `AVPlayerViewController`. When you slide your finger up and away from the slider, the rate at which the time changes reduces. The further away you are, the slower it gets.

{% include gifv.html src="/assets/2020-03-04-framegrabber.mp4" caption="Variable scrubbing speeds in Frame Grabber." %}

[Frame Grabber](https://github.com/arthurhammer/FrameGrabber) is all about picking the right moment, down to the exact frame. It's the perfect fit for this behavior and I just shipped it in an update. Selecting frames is now a lot easier.

In this post, I'll outline how to implement this interaction. The result is `ScrubbingSlider`, a drop-in `UISlider` subclass that adds variable scrubbing speeds.

You can [find the full implementation here](https://github.com/arthurhammer/blog-example-code/blob/master/2020-03-04-uislider-with-scrubbing-speeds/ScrubbingSlider/ScrubbingSlider.swift) including a small sample project.

**Related Work**: Ole Begemann wrote about a similar solution a looong time ago. [Check it out here](https://oleb.net/blog/2011/01/obslider-a-uislider-subclass-with-variable-scrubbing-speed/).

## Public API

Let's work backwards from how we're going to use this class to how it is implemented.

`ScrubbingSlider` exposes two new properties. One configures the discrete speeds the slider uses and the other one returns the current speed:

{% highlight swift %}
class ScrubbingSlider: UISlider {
    var scrubbingSpeeds: [ScrubbingSpeed]
    private(set) var currentScrubbingSpeed: ScrubbingSpeed
}
{% endhighlight %}

A scrubbing speed is made up of two parts:

1. The fraction of the normal `UISlider` speed to use. 1 is normal speed, 0.5 is half that speed and so on.
2. The vertical distance the user's finger has to move away from the slider for it to take effect.

{% highlight swift %}
struct ScrubbingSpeed {
    let speed: Float
    let verticalDistance: CGFloat
}
{% endhighlight %}

The slider's default configuration matches that of `AVPlayerViewController:`

{% highlight swift %}
extension ScrubbingSpeed {
    static let defaultSpeeds = [
        ScrubbingSpeed(speed: 1, verticalDistance: 0),
        ScrubbingSpeed(speed: 0.5, verticalDistance: 50),
        ScrubbingSpeed(speed: 0.25, verticalDistance: 100),
        ScrubbingSpeed(speed: 0.1, verticalDistance: 150)
    ]
}
{% endhighlight %}

### Usage

The class is designed as a drop-in replacement for `UISlider` without additional setup. In a view controller:

{% highlight swift %}
func viewDidLoad() {
    super.viewDidLoad()

    slider.scrubbingSpeeds = [...]  // optional
    slider.addTarget(self, action: #selector(sliderDidScrub), for: .valueChanged)
}

@objc func sliderDidScrub(_ sender: ScrubbingSlider) {
    print("Current value:", sender.value)
    print("Current speed:", sender.currentScrubbingSpeed)  // optional
}
{% endhighlight %}

We use the `valueChanged` event to check for both the current value and the current scrubbing speed. Since the speed is always tied to a scrub interaction, there is no need to implement a separate update mechanism such as delegation.

## Implementation

As soon as the user touches the slider's knob, we want to hook in and customize what happens. Our extension points are therefore the slider's touch handlers. For subclasses of `UIControl` (including `UISlider`), these are:

- `beginTracking(_:with:)`
- `continueTracking(_:with:)`
- `cancelTracking(_:with:)`
- `endTracking(_:with:)`

Three of those are simple: In `beginTracking`, we cache the current value as we need it later. In `cancelTracking` and `endTracking`, we set the current scrubbing speed back to its default value.

The meat of the work is in `continueTracking`, called repeatedly when the user moves her finger. Each time it is called, we want to update two things:

1. The current speed
2. The current value (adjusted by the current speed)

The following schematic demonstrates what we need to calculate:

{% include figure.html src="/assets/2020-03-04-scrub.jpg" caption="" alt="Schematic of updating speed and value of ScrubbingSlider." %}

In code:

{% highlight swift %}
override func continueTracking(_ touch: UITouch, with event: UIEvent?) -> Bool {
    guard isTracking else { return false }

    let touchLocation = touch.location(in: self)
    let previousLocation = touch.previousLocation(in: self)

    let previousSpeed = currentScrubbingSpeed
    currentScrubbingSpeed = scrubbingSpeed(for: touchLocation)

    let previousValue = value
    let valueAdjustment = self.valueAdjustment(for: touchLocation, relativeTo: previousLocation)
    let speedAdjustment = currentScrubbingSpeed.speed * valueAdjustment
    let thumbAdjustment = self.thumbAdjustment(for: touchLocation, relativeTo: previousLocation)

    unadjustedValue = unadjustedValue + valueAdjustment
    value = value + speedAdjustment + thumbAdjustment

    if isContinuous {
        sendActions(for: .valueChanged)
    }

    generateFeedbackIfNecessary(forPreviousValue: previousValue, previousSpeed: previousSpeed)

    return true
}
{% endhighlight %}

One thing I haven't explained yet is the role of `thumbAdjustment`. Notice how in a normal `UISlider`, the user's finger is always right above the knob in a straight line. That's not the case in `ScrubbingSlider`. Due to variable speeds, the finger can be to the left or right of the knob.

What we now want is this: When the user's finger moves back down towards the slider, the knob rushes towards it so both meet at the same spot. The closer the finger is to the slider, the faster the knob moves. Schematically:

{% include figure.html src="/assets/2020-03-04-scrub2.jpg" caption="" alt="Schematic of updating speed and value of ScrubbingSlider." %}

This adjustment value is added to create the slider's final value.

Finally, we generate a haptic feedback when:

- the current speed changes
- the user hits the start or the end of the slider.

This helps the user feel connected to her interaction with the slider.

For all details, [please check out the full implementation](https://github.com/arthurhammer/blog-example-code/blob/master/2020-03-04-uislider-with-scrubbing-speeds/ScrubbingSlider/ScrubbingSlider.swift).

## Considerations

### Discoverability

On its own, this interaction is not very discoverable to the average user. The haptic feedback gives a good indication that something is happening but it's not sufficient.

Apple's `AVPlayerViewController` implementation shows an explanatory tooltip but only when the user long presses on the slider without moving the finger.

In Frame Grabber, I opted to show an indicator when the user changes speed for the first time during an interaction. After that, it is shown for the remaining interaction. In direct tests with users it was very likely for them to discover it. Users often hit the first speed boundary just by sliding normally. From there, haptic feedback and the speed indicator should do the rest. Making it even more explicit would probably start to annoy the user.


### Accessibility

The subclass inherits all built-in accessibility capabilities of `UISlider` and is fully functional in that regard. What's left to do is to expose the different scrubbing speeds to accessibility users.