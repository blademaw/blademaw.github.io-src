Title: Setting up & Customizing Liquid Tags in Pelican
Date: 2021-09-21 16:00
Tags: python, pelican, plugins
[id1]: ## "your hover text"

## A word on `liquid-tags` and Pelican plugins

Without delving in too deep, <abbr title="'Liquid tags' are the actual tag objects, whereas 'liquid-tags' is the Pelican plugin">Liquid Tags</abbr> are the saving grace of media integration in Pelican — they integrate seamlessly with Markdown or reStructuredText, and can be customized. For example, the following:

    :::liquid
    {% literal notebook my-jupyter-notebook.ipynb cells[2:3]  %}

displays cells 2–3 of a Jupyter notebook:

{% notebook representing-problems.ipynb cells[2:3]  %}

They follow a simplistic structure — enclosed in curly braces and percent signs, the first argument is the type of liquid tag to be integrated, and the following arguments are content parameters, usually a directory to a file, and aesthetic tuners.

They use regular expressions to match arguments to groups, generating HTML tags appropriately. Created by one of my favorite data scientists, [Jake VanderPlas](https://github.com/jakevdp), they are an ingenious invention that are difficult to live without once you start using them.

Unfortunately, they **do not come standard** with Pelican, and must be installed and recognized by Pelican in order to be used within articles. Choosing which method of installation and which version of `liquid-tags` to install can be time-consuming, so it is my aim in this brief article to simplify the process for any future users.

## Installing `liquid-tags`

From what I can tell, it used to be that **all** Pelican plugins had to be cloned from [this massive repo](https://github.com/getpelican/pelican-plugins) and stored locally in a `/plugins/` directory to be used. Recently however, the Pelican Plugins organization has attempted to streamline the plugin acquisition pipeline by migrating plugins to a [new organization](https://github.com/pelican-plugins).

The majority of plugins can now be installed via a simple `pip install <plugin>` and specified in your `pelicanconf.py` for use without hassle. This is a good and viable option **if you do not wish to customize the tags at all**. However, if you **do** want some customization, you'll need to go local.

The most up-to-date version of liquid-tags should be installed, available [here](https://github.com/pelican-plugins/liquid-tags).

For no customization, a simple

    :::zsh
    $ python -m pip install pelican-liquid-tags

will suffice. Then you can specify the plugin and choose your tags in order to use it in your `pelicanconf.py` as such:

    :::python
    PLUGINS = ['liquid-tags']
    LIQUID_TAGS = ["literal", "video", "img", "include_code"]

<br/>
For local installations, create a `/plugins/` subdirectory in your `pelican` root directory if you don't already have one, and then clone the `liquid-tags` repo into a folder:

    :::zsh
    $ git clone https://github.com/pelican-plugins/liquid-tags.git pelican-plugins/liquid_tags

Here I've created an extra subdirectory `/plugins/pelican-plugins/` to match the legacy system of importing plugins. Once you've cloned the repo, move all the contents of `liquid_tags/pelican/plugins/liquid_tags/` to the folder you cloned liquid-tags to. My final folder looks like this:

    :::bash
    main_dir
    ├── ...
    ├── content
    │   ├── ...
    ├── output
    │   ├── ...
    └── plugins
        └── pelican-plugins
            └── liquid_tags
                ├── img.py
                ├── notebook.py
                └── ...

Then add the source directory to your `pelicanconf.py` for liquid-tags and import the tags you want to use (with the local directory, these must be **individually specified and added** to `PLUGINS` prefixed by `liquid_tags.`):

    :::python
    PLUGIN_PATHS = ['./plugins/pelican-plugins']
    PLUGINS = ['render_math', 'liquid_tags.img',
             'liquid_tags.notebook', 'liquid_tags.literal']

Now you can begin using the tags. Regarding documentation of specific tags, I find reading the header in the tag's `.py` file easiest, but you can view the `README` for `liquid-tags` [here](https://github.com/pelican-plugins/liquid-tags).

## Customizing tags
As mentioned, liquid tags substitute the written tag in Markdown by matching a regular expression to the given arguments, and inserting them into appropriate groups in an HTML snippet. If you'd like to add your own arguments to tags, create your own, or edit the HTML outputted by a tag, you can edit the appropriate `.py` file.

The good news is most of the legwork is already done for you — the first step is customizing the regular expression to match. It'll look something like this:

    :::python
    AUDIO = re.compile(
        r"(/\S+|https?:\S+)(?:\s+(/\S+|https?:\S+))?(?:\s+(/\S+|https?:\S+))?"
    )

Once you've altered it to your liking, check how the file splits and assigns groups, which will depend on the tag. Most files have a `for` loop that collects arguments into a dictionary `attrs` where `(key, value)` pairs are in the format `(regex_group, matched_string)`.

All tags work by returning the HTML to be put in your page as a string. Since string manipulation is especially easy in Python, the rest of the work is really just formatting your HTML string by inserting the right dictionary values in the right places.

### Example — altering `img.py` for figures
While the regular `img` tags are fine, I wanted a styled version for figures that needed captions, and images of interest. I could have created a separate `figure.py` liquid tag, but I opted for editing the `img.py` file.

This way, I can embed regular images like such:

{% img /images/stochastic_lotka_volterra.png 450 300 "" "A stochastic Lotka-Volterra model" %}

Or highlight images with a subtle [styled background](https://heiswayi.nrird.com/image-caption-using-liquid-syntax) and padding:

{% img styled /images/stochastic_lotka_volterra.png 450 300 "" "A stochastic Lotka-Volterra model" %}

Or add a figure and source, if necessary:

{% img styled /images/stochastic_lotka_volterra.png 450 300 "Figure 1. A stochastic Lotka-Volterra model" "A stochastic Lotka-Volterra model" "#" %}

To accomplish this, I tweaked the `img.py` file:

I first changed the expression to match from

    :::bash
    (?P<class>\S.*\s+)?(?P<src>(?:https?:\/\/|\/|\S+\/)\S+)(?:\s+(?P<width>\d+))?(?:\s+(?P<height>\d+))?(?P<title>\s+.+)?

to:

    :::bash
    (?P<class>\S*\s)?(?P<src>(?:https?:\/\/|\/|\S+\/)\S+)(?:\s+(?P<width>\d+))?(?:\s+(?P<height>\d+))?(?P<title>\s+.+)?

which limits the tag to one class name. The figure caption, alt text, and source are all captured in the `<title>` group.

Then, I altered the function body to parse the regex like so:

{% include_code img_ex.py lang:python lines:72-85 :hideall: %}

which matches a title, alt text, and source if possible — if not, it tries to match a title and alt text. If it can't match either of these and just finds a title (minimum requirement) it'll assign the alt text the title.

Then the beginning of the HTML is specified:

{% include_code img_ex.py lang:python lines:87-88 :hideall: %}

which defines `tag_out`, the output HTML, and `fig_tag`, the caption to be displayed.

{% include_code img_ex.py lang:python lines:92-98 :hideall: %}

The above code then adds a caption to the figure if necessary, and a class if given in the liquid tag. The following code is from the original plugin:

{% include_code img_ex.py lang:python lines:100-103 :hideall: %}

which appends all additional arguments in the liquid tag to the HTML `<img>` tag. Finally, the source is added if supplied, and all tags are closed:

{% include_code img_ex.py lang:python lines:105-114 :hideall: %}

So in the end, the three images above can then be displayed using the following tags:

    :::liquid
    {% literal img /images/stochastic_lotka_volterra.png 450 300 "" "A stochastic Lotka-Volterra model" %}
    
    {% literal img styled /images/stochastic_lotka_volterra.png 450 300 "" "A stochastic Lotka-Volterra model" %}

    {% literal img styled /images/stochastic_lotka_volterra.png 450 300 "Figure 1. A stochastic Lotka-Volterra model" "A stochastic Lotka-Volterra model" "#" %}

## Conclusion
Liquid tags in Markdown (\[un\]confusingly supplied by the `liquid-tags` plugin) are a great way to seamlessly incorporate multimedia in your Markdown articles or pages. In short, acquiring them through `pip` is your best bet if you plan on using them as-is, but to alter their behavior you're going to need to peek behind the curtain.

Luckily, with some regex, they are easy enough to tweak (and possibly create, if you're brave enough!). If you'd like to try my slightly edited `img.py` file discussed in the example, you can download it [here](/features/code/img_ex.py).