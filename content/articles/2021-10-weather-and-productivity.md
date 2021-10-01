Title: Does the Weather Affect my Productivity?
Date: 2021-10-02 16:00
Tags: statistics, python, r
slug: weather-and-productivity

<figure class="styled"><img class="styled" src="/images/lazy_summer.jpeg" width="350" height="200" title="A lazy summer morning, evening?" alt="A lazy summer morning, evening?"><figcaption>Image from The New Yorker <a href="https://www.newyorker.com/tech/annals-of-technology/why-summer-makes-us-lazy">(source)</a></figcaption></figure>

For most of us, the environment in which we work is an extremely impactful factor that contributes to our capacity for productivity. Lighting, odor, temperature, furniture — these are parameters of our environment **we can tune** to allow ourselves to work better.

But we can't control _everything_, that would be cheating. Weather conditions are an external factor that may or may not affect productivity: [one study](https://www.apa.org/pubs/journals/features/apl-a0035559.pdf) suggests worse weather is correlated with higher productivity.

This got me thinking — could I conduct a toy case-study on myself? Where would I get the data? Suddenly, I remembered in the months of study-leave leading up to my International Baccalaureate (IB) exams, I had tracked **my time spent studying and doing homework** using [Toggl](https://toggl.com/).

<figure class="styled"><img class="styled" src="/images/toggl-time.png" width="350" height="260" title="My hours logged leading up to the IB examinations" alt="My hours logged leading up to the IB examinations"></figure>

So I had 135 hours' worth of data over March, April, and May 2019 that could be downloaded as a `.csv` — not bad. Also, at the time, I was **totally blind** to what I would do with the data, meaning I possibly ducked data collection biases by being naïve! I wagered it wouldn't be too hard to find the weather data, and the rest of this blog post is what ensued.
<!-- PELICAN_END_SUMMARY -->

{% notebook 2021-10-weather-productivity.ipynb cells[6:] %}