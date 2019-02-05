---
title: Visualizing My Photo Library
description: Spotting trends in 17k photos.
---

**Note**: There's an interactive version of this post [as an Observable notebook here](https://beta.observablehq.com/d/2b277150e16e933e).

---

My iCloud Photo Library where I keep the majority of my photos keeps growing steadily. Currently, there are a total of **18868 photos** in there.[^1] I wanted to get an overview of my photo habits by charting how and when I take photos.

## Photos by Year and Month

{% include figure.html src="/assets/2018-12-08-year.jpg" caption="Number of photos by year and month. Click for full image." alt="Number of photos by year and month" %}

Let's start with the number of photos I took each year. It is displayed in the chart at the top. The trend is obvious, I take more photos each year. While 2012 to 2016 saw moderate growth, I was quite surprised by the explosion in 2017 and 2018.

I see a few reasons for this: Obviously, I just take more photos in general. More specifically, I stopped filtering myself. I now take a lot of pictures of everday mundane things for archival purposes, like a visual diary. Ten years down the road, I want to get a good feel of how my life is today. And finally, I started asking friends and family to share their photos with me more regurlarly.

The bottom right chart shows photos by month. December is the clear winner and reflects the collected Christmas and New Year's Eve photos from our family gatherings. Apparently I don't take many photos in the cold months of January and February.

The chart on the bottom left combines both charts and gives photos per year and month. Christmas time each year is noticeable again (and increasing each year) but I also have yearly photos in April from my birthday.

## Photos by Weekday and Time of Day

{% include figure.html src="/assets/2018-12-08-time.jpg" caption="Number of photos by weekday and time of day." alt="Number of photos by weekday and time of day" %}

I was particularly interested in *when* I take most photos, i.e. which weekday or time of day. The bottom right chart clearly highlights Saturday as my photo day of choice. Makes sense since that's when most exciting things happen. Friday and Sunday, too, stand out from the regular workdays.

The chart on the top shows at which time during the day I take most photos. It slowly ramps up from late morning and peaks from early afternoon to evening. During nights I tend to sleep (or maybe am awake but don't shoot many photos). Surprisingly, in all these years, I've only managed to take six photos between four and five a.m.

From the bottom left chart we can see that at least on Fridays and Saturdays, I do take some late night and early morning photos.

## Every Photo I Have Ever Taken

{% include figure.html src="/assets/2018-12-08-dots.jpg" caption="Click for full image." alt="" %}

Here is one dot for every photo in my library. Looking at this feels weirdly intimate. These aren't even photos, just dots but they represent a lot of individual moments in my life. It goes to show how much meaning there is in metadata alone.

In the interactive notebook you can even zoom into the chart and see when I took photos on individual days. there

This chart again visualizes the increase in photo density over time.

## Data

The data is exported from my iCloud Photo Library on my iPhone. I used the [Pythonista iOS app](http://omz-software.com/pythonista/) and the Photos API to export some metadata for each photo. You can [find the script and dataset here](https://gist.github.com/arthurhammer/a861fc9a91669397a5cc70fc9d8ebedd).

Charts were created with the excellent [Vega-Lite library](http://vega.github.io/vega-lite/).

## Conclusion

This was a fun way to make some temporal sense of my photo library.

In this post, I only considered photos by creation date. In the future, I could include and visualize additional metadata for each photo such as:

- Chart photos by types (photo, video) and subtypes (live photo, slow motion video etc.), by camera model, by whether the photo is favorited etc.
- Filter charts by photo type, subtype, camera model, favorites etc.
- Map photos by geolocation.

Additionally, I could add some crossfilters. For example, see how weekday and time of day charts change for each year. There are a lot of dimensions for simple data like this.

Photo libraries used to be nothing more than sequences of photos. But with evergrowing libraries spanning decades and potentially reaching hundreds of thousands of photos, it will become increasingly harder to keep an overview. Apple, Google and others have noticed this and are heavily ramping up their Machine Learning and other automated photo analysis approaches (face and object recognition, smart photo clustering, memory reminders, filtering photos across multiple dimensions etc.). I'm excited where this is going and how we'll interact with our photo libraries in the future.

[^1]: Not all of the photos in my library were taken by me and not all photos I've ever taken are in there. And for simplictiy, I used the term "photo" to denote any type of item in my library be it photo, video, GIF, audio etc.
