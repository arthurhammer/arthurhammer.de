---
title: Visualizing My Photo Library
description: Spotting trends in 19k photos.
---

I keep the majority of my photos in my iCloud photo library. It keeps growing steadily with a total of 18 868 photos in there currently. I wanted to make some sense of all that data and see my photo-taking habits visualized.

So let's chart how and when I take photos.

 <!--more-->

**Note**: Check out an interactive version of this post [as an Observable notebook here](https://beta.observablehq.com/d/2b277150e16e933e).

## By Year and Month

{% include figure.html src="/assets/2018-12-08-year.jpg" caption="Number of photos by year and month. Click for full image." alt="Number of photos by year and month" %}

We start with the number of photos I took each year.[^1] It is displayed in the chart at the top. The trend is obvious, I take more photos each year. While 2012 to 2016 saw moderate growth, I was quite surprised by the explosion in 2017 and 2018.

I see a few reasons for this: Obviously, I just take more photos in general. But I also stopped filtering myself. I now take a lot of pictures of everday mundane things for archival purposes, like a visual diary. Ten years down the road, I want to get a good feel of how my life is today. Finally, I started asking friends and family to share their photos with me more regurlarly.

The bottom right chart shows photos by month. December is the clear winner and reflects the collected Christmas and New Year's Eve photos from our family gatherings. Apparently I don't take many photos in the cold months of January and February.

The chart on the bottom left combines both charts and gives photos per year and month. Christmas time each year is noticeable again (and increasing each year) but I also have yearly photos in April from my birthday.

## By Weekday and Time of Day

{% include figure.html src="/assets/2018-12-08-time.jpg" caption="Number of photos by weekday and time of day." alt="Number of photos by weekday and time of day" %}

I was particularly interested in *when* I take most photos, i.e. which weekday or time of day. The bottom right chart clearly highlights Saturday as my photo day of choice. Makes sense since that's when most exciting things happen. Friday and Sunday, too, stand out from the regular workdays.

The chart on the top shows at which time during the day I take most photos. It slowly ramps up from late morning and peaks from early afternoon to evening. During nights I tend to sleep (or maybe am awake but don't shoot many photos). Surprisingly, in all these years, I've only managed to take six photos between four and five a.m.

From the bottom left chart we can see that at least on Fridays and Saturdays, I do take some late night and early morning photos.

## Every Photo I Have Ever Taken

{% include figure.html src="/assets/2018-12-08-dots.jpg" caption="The dots are colored by year." alt="Every photo I have ever taken." %}

Here is one dot for every photo in my library. Again, you can see the increase in photo density over time.

Looking at this chart feels weirdly intimate. These are just dots—not even pictures—but they represent a lot of individual moments in my life. It gets even more intimate when we check what I've been up to on individual days:

{% include figure.html src="/assets/2018-12-08-day.jpg" caption="My weekend trip to Berlin in photos." alt="My weekend trip to Berlin in photos." %}

Just by looking at the photo pattern from my Berlin trip, I start to remember individual moments. Friday is empty as I was working late, then driving to Berlin and arriving at night. Saturday I explored the city. Sunday morning I watched the Berlin Marathon, in the afternoon I visited a friend.

It goes to show how much meaning there is in metadata alone, and that's just for dates. The photos I take usually include a geolocation tag as well. Mapping out photos by date and location could give me a reasonably detailed account on where I've been on any given day. For my Berlin trip, I was taken back to the places, museums and restaurants I visited. Without once looking at a single picture.

## Data

The data is exported from my iCloud photo library on my iPhone. I used the [Pythonista iOS app](http://omz-software.com/pythonista/) and PhotoKit to export relevant metadata for each photo. You can [find the script and the full dataset here](https://gist.github.com/arthurhammer/a861fc9a91669397a5cc70fc9d8ebedd), don't be creepy.

Charts were created with the excellent [Vega-Lite library](http://vega.github.io/vega-lite/).

## Conclusion

This was a fun way to make some temporal sense of my photo library.

In this post, I analyzed photos mostly by creation date. In the future, I could include and visualize additional metadata for each photo such as:

- Chart photos by types (photo, video) and subtypes (live photo, slow motion video etc.), by camera model, by whether the photo is favorited etc.
- Filter charts by photo type, subtype, camera model, favorites etc.
- Map photos by geolocation.

Additionally, I could add some crossfilters. For example, see how weekday and time of day charts change for each year. There are a lot of dimensions for simple data like this.

Photo libraries used to be simple sequences of photos, [not anymore](https://oleb.net/2018/photos-data-model/). With evergrowing libraries spanning decades and potentially reaching hundreds of thousands of photos, it will become increasingly hard to keep an overview. The purely manual approach we're used to in finding the data we're looking for is probably not scalable. Apple, Google and others have noticed this and are ramping up their machine learning and other automated photo analysis approaches.[^2] I'm excited where this is going and how we'll interact with our photo libraries in the future.

[^1]: Not all of the photos in my library were taken by me and not all photos I've ever taken are in there. And for simplictiy, I used the term "photo" to denote any type of item in my library be it photo, video, GIF, audio etc.
[^2]: Already, there are things like face and object recognition, smart photo clustering, moment summaries, memory reminders, sharing suggestions, filtering photos across multiple dimensions and a ton more.