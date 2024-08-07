title: About
slug: about
Template: about

<img src="/images/me.jpg" align="left" width="150" style="padding-right:20px;"/>
Hi there—my name is Jack, and I'm a postgraduate computer science student at the University of Melbourne, and a Financial Risk Analyst at Deloitte. When I'm not occupied with school and work, I enjoy crafting side-projects that let me explore and experiment with interesting topics. Sometimes I end up uploading them to this blog and talking about them.
<br/>

**Details about this blog**:

* This blog is built with [Pelican](https://blog.getpelican.com/){:target="_blank"}, using a (slightly tweaked) theme from [Jake VanderPlas](https://github.com/jakevdp/jakevdp.github.io-source){:target="_blank"}.
* Images on this blog such as the following: {% img styled /images/lorenz.png 300 225 "Figure 1: The Lorenz System" "" %} are implemented using a [modified version]({filename}/articles/customizing-liquid.md) of Jake VanderPlas' [Liquid Tags](https://github.com/pelican-plugins/liquid-tags){:target="_blank"} and styling inspired by [Heiswayi Nrird](https://heiswayi.nrird.com/image-caption-using-liquid-syntax){:target="_blank"}.
* Jupyter notebooks are integrated with a custom version of liquid tags—I'm using an environment with [the following](/features/files/requirements.txt) build requirements, and my `liquid_tags` plugin directory has an additional `core.py` file from the legacy `ipynb.liquid` Pelican plugin and a modified `notebook.py`. You can click [here](/features/code/core.py) and [here](/features/code/notebook.py) to download the respective files.
* This blog's name is a pun on the programming paradigm "divide and conquer," and I *would* change it to something less shameful, but it is simply too much hassle to update all of the Pelican source files.
