---
title: Observing Nested Properties in Combine
description: A Swift-native alternative to key-value observing.
---

[Key-value observing](https://developer.apple.com/documentation/swift/cocoa_design_patterns/using_key-value_observing_in_swift) is an ancient technology on Apple platforms. It allows objects to be notified of changes to properties of other objects. Working with KVO in Swift has always been cumbersome. It's only available in `NSObject` subclasses, making it impossible to use as your one-stop binding solution.

[Combine](https://developer.apple.com/documentation/combine), Apple's new [functional reactive](https://gist.github.com/staltz/868e7e9bc2a7b8c1f754) framework, promises to change that. It is fully native in Swift and observing properties is one of its many use cases.

Replacing KVO with Combine, however, is not without gotchas. What KVO gets right is that it makes it easy to observe *nested* properties. With Combine, it's more difficult.

In this post, I'll explain why that is and how to bridge the gap.

<!--more-->


## What We Want to Do

Say, we have a video player app and want to display the current video title in a label. The setup looks like this:

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

Our goal is to keep the video title and the label in sync. In the view controller, we want to observe the nested property `playbackController?.player?.videoTitle` and update `titleLabel` with its value. This is called a binding.


### Nesting

When observing nested properties, a binding should have one important feature: It needs to be robust against changes to intermediate properties.

Let me illustrate with an example.

Assume we've set up the initial binding. At some point, we replace the playback controller's player:

{% highlight swift %}
let oldPlayer = playbackController.player
let newPlayer = Player()
playbackController.player = newPlayer
{% endhighlight %}

What do we expect to happen? We expect the video title label to display `newPlayer.videoTitle`, not `oldPlayer.videoTitle`. In other words, the binding reports the value of `playbackController?.player?.videoTitle` independent of which specific intermediate instances it is attached to.

The same goes for `nil`. When the player becomes `nil` so should the video title.

This feature has a big advantage. It makes our code simpler and more maintainable. We can define the binding only once when we create the view controller and let any changes propagate automatically.


## Key-Value Observing

This is easy to do with key-value observing. In fact, it's its prime use case. KVO allows us to observe *key paths* or chains of nested properties as follows:

{% highlight swift %}
var token: Any?

func bindLabel() {
    token = observe(\.playbackController?.player?.videoTitle, options: .initial) { viewController, _ in
        viewController.titleLabel.text = viewController.playbackController?.player?.videoTitle
    }
}
{% endhighlight %}

KVO has a big drawback: It's only available in `NSObject` subclasses and properties marked with `@objc dynamic`. We can't use KVO when working with plain Swift types. It's inherently tied to Objective-C.

As a result, developers had to roll their own Swift binding solution while waiting for a native one. With Combine, it finally arrived.


## Combine

Let's explore how we can create our binding in Combine.

The basic building blocks in Combine are [publishers](https://developer.apple.com/documentation/combine/publisher). A publisher emits values over time, in our case when a property changes.

To make a property observable in Combine, we create a publisher for it. And to make an entire chain of nested properties observable, we need to create a publisher for each one.

We can do this conveniently by marking all properties with [`@Published`](https://developer.apple.com/documentation/combine/published).


### Non-Optionals

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

Note the use of `$`. It refers to the property's publisher as opposed to its value.

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


### Optionals

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

With both extensions in place, we can finally create our binding as follows:

{% highlight swift %}
var token: Any?

func bindLabel() {
    token = $playbackController
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
