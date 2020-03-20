---
title: Observing Nested Properties in Combine
description: A Swift-native alternative to key-value observing.
---

[Combine](https://developer.apple.com/documentation/combine) is the new cool kid on the block. It's Apple's new [functional reactive](https://gist.github.com/staltz/868e7e9bc2a7b8c1f754) framework. Only available in Swift and quite a departure from previous first-party paradigms.

I wanted to see how Combine stacks up to [key-value observing](https://developer.apple.com/documentation/swift/cocoa_design_patterns/using_key-value_observing_in_swift) when it comes to observing properties. Key-value observing makes it easy to observe values along nested properties.

It's not immediately clear how to do the same in Combine. We'll explore this topic in this post.

<!--more-->


## What We Want to Do

Say, we have a video player app and want to display the current video title in a label. It's set up like this:

{% highlight swift %}
class PlayerViewController: UIViewController {
    var playbackController: PlaybackController?
    let titleLabel: UILabel
}

class PlaybackController {
    var player: Player?
}

class Player {
    var videoTitle: String
}
{% endhighlight %}

In the view controller, we want to keep the video title and the label in sync. That is, we want to observe the property chain `playbackController?.player?.videoTitle` and update `titleLabel` with its value. This is called a binding.


### Binding Once

It is important for the binding to adapt to changes to intermediate properties.

Let's say we replace the playback controller's player. We want the binding to report the title of that new player without additional work on our part. In case the player becomes `nil`, the binding should also report `nil`.

This makes our code simpler and more maintainable. We can define the binding only once when we create the view controller. Properties might still be `nil` at that point. But as soon as we inject values, they propagate automatically.

{% highlight swift %}
override func viewDidLoad() {
    super.viewDidLoad()
    bindLabel()
}

func bindLabel() {
    // Set up binding.
}
{% endhighlight %}


## Using Key-Value Observing

This is the prime use case of [key-value observing](https://developer.apple.com/documentation/swift/cocoa_design_patterns/using_key-value_observing_in_swift). It allows us to observe values along a key path, i.e. along a chain of properties.

`NSObject` provides a [Combine publisher](https://developer.apple.com/documentation/objectivec/nsobject/keyvalueobservingpublisher) that integrates with key-value observing:

{% highlight swift %}
var cancellable: AnyCancellable?

func bindLabel() {
    cancellable = publisher(for: \.playbackController?.player?.videoTitle)
        .sink { [weak self] title in
            self?.titleLabel.text = title
        }
}
{% endhighlight %}

This has a big drawback: Key-value observing is tied to Objective-C. It's only available in `NSObject` subclasses and properties exposed to Objective-C via `@objc dynamic`.

We can't use it when working with plain Swift types.


## Using Plain Combine

To make properties observable in Combine, we use [publishers](https://developer.apple.com/documentation/combine/publisher). A publisher emits values over time, in our case when a property changes.

To make an entire chain of properties observable, we need to create a publisher for each one.

We can do this conveniently by marking all properties with [`@Published`](https://developer.apple.com/documentation/combine/published). The `@Published` attribute creates a publisher for its property. To refer to the publisher as opposed to the value, we prepend `$` to the property name.


### Handling Non-Optionals

First, let's simplify our assumptions. Consider the case where all properties along the chain are non-optionals:

{% highlight swift %}
@Published var playbackController: PlaybackController
@Published var player: Player
@Published var videoTitle: String
{% endhighlight %}

We then create our binding as follows:

{% highlight swift %}
$playbackController
    .flatMap { $0.$player }
    .flatMap { $0.$videoTitle }
    .sink { [weak self] title in
        self?.titleLabel.text = title
    }
{% endhighlight %}

[`flatMap`](https://developer.apple.com/documentation/combine/publisher/3204712-flatmap) takes the value from the previous publisher and returns a new one. The playback controller publisher is successively mapped into the video title publisher.

Compare this with the following:

{% highlight swift %}
playbackController.player.$videoTitle
    .sink { [weak self] title in
        self?.titleLabel.text = title
    }
{% endhighlight %}

This only binds the *current* playback controller's *current* player's video title. When either changes, the binding becomes outdated.

This is also incorrect:

{% highlight swift %}
$playbackController
    .map { $0.player }
    .map { $0.videoTitle }
    .sink { [weak self] title in
        self?.titleLabel.text = title
    }
{% endhighlight %}

This sink is only triggered when the playback controller instance changes. Changes to the player or video title are not recorded.

What the latter two get wrong is that they operate on the level of values. The correct solution above operates on the level of publishers. To observe a chain of properties in Combine, we need an unbroken chain of publishers handing down their values.


### Handling Optionals

With optionals, it's trickier. Let's add them back in:

{% highlight swift %}
@Published var playbackController: PlaybackController?
@Published var player: Player?
@Published var videoTitle: String
{% endhighlight %}

The binding from above now looks like this:

{% highlight swift %}
$playbackController
    .flatMap { $0?.$player }      // Error: Value of optional type _? must be unwrapped to a value of type _.
    .flatMap { $0?.$videoTitle }  // Error: Value of optional type _? must be unwrapped to a value of type _.
    .sink { [weak self] title in
        self?.titleLabel.text = title
    }
{% endhighlight %}

This doesn't compile. Since `playbackController` is an optional, the input to `flatMap` is too and so is its output. `flatMap`, however, only accepts concrete return values.

What we need to do is provide an alternative publisher should `playbackController` be `nil`. The solution is to replace a `nil` publisher with a publisher that emits `nil`:

{% highlight swift %}
$playbackController
    .flatMap {
        $0?.$player.eraseToAnyPublisher()
            ?? CurrentValueSubject(nil).eraseToAnyPublisher()
    }
    .flatMap {
        $0?.$videoTitle.eraseToAnyPublisher()
            ?? CurrentValueSubject(nil).eraseToAnyPublisher()
    }
    .sink { [weak self] title in
        self?.titleLabel.text = title
    }
{% endhighlight %}

[`eraseToAnyPublisher`](https://developer.apple.com/documentation/combine/publisher/3241548-erasetoanypublisher) is required to reduce both publishers to the same type.

We've pushed the optional one level deeper. The difference is important: The chain of publishers remains unbroken. Should any value along the chain be `nil`, we propagate it downstream.


## Extending `flatMap`

For longer chains, this gets unruly very quickly. It is better extracted into an extension. I chose to overload the `flatMap` operator. Another solution could be to write a custom proxy publisher to wrap optional publishers.

{% highlight swift %}
extension Publisher {

    func flatMap<P, T>(_ transform: @escaping (Output) -> P?) -> Publishers.FlatMap<AnyPublisher<T?, Failure>, Self>
        where P: Publisher, P.Output == T?, Failure == P.Failure {

        flatMap {
            transform($0)?.eraseToAnyPublisher()
                ?? CurrentValueSubject(nil).eraseToAnyPublisher()
        }
    }
}
{% endhighlight %}

The signature looks more complex than it is. The important thing is that the output `Output` of the current publisher is the input of the `transform` closure which converts it into a new *optional* publisher `P?`.

In the case above, the output of that new publisher is an optional itself (`P.Output == T?`). The case where it is not must be handled in a separate overload (`P.Output == T`):

{% highlight swift %}
extension Publisher {

    func flatMap<P, T>(_ transform: @escaping (Output) -> P?) -> Publishers.FlatMap<AnyPublisher<T?, Failure>, Self>
        where P: Publisher, P.Output == T, Failure == P.Failure {

        flatMap {
            transform($0)?.map { $0 }.eraseToAnyPublisher()
                ?? CurrentValueSubject(nil).eraseToAnyPublisher()
        }
    }
}
{% endhighlight %}

This is the same except for `map`. Its job is to raise the new publisher's output type `T` to the required `T?`.

## Wrapping Up

With both extensions in place, we can finally solve our binding problem as follows:

{% highlight swift %}
var cancellable: AnyCancellable?

func bindLabel() {
    cancellable = $playbackController
        .flatMap { $0?.$player }      // First overload: player is optional
        .flatMap { $0?.$videoTitle }  // Second overload: videoTitle is non-optional
        .sink { [weak self] title in
            self?.titleLabel.text = title
        }
}
{% endhighlight %}

So what have we achieved here?

We have shown how to observe nested properties with Combine. We can set up the binding once and handle changes to intermediate properties automatically. This makes code simple and maintainable.

The method behaves similar to key-value observing. But unlike key-value observing, it is available in plain Swift types. Setting up the solution proved to be a bit of work, though. It required us to patch Combine's gaps when it comes to optional publishers.
