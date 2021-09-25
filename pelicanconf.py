#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Jack Oliver'
SITENAME = 'Divide & Ponder'
SITESUBTITLE = 'Vague ventures stumbling through computer science'
SITEURL = 'https://blademaw.github.io'
TIMEZONE = 'Australia/Melbourne'
DEFAULT_LANG = 'en'

PATH = 'content'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Article URL Settings
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'
DEFAULT_PAGINATION = 10

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = './theme/'

MARKUP = ('md', )

PLUGINS = ['render_math', 'liquid_tags.img',
             'liquid_tags.notebook', 'liquid_tags.literal',
             'liquid_tags.include_code',
             'liquid_tags.vega']
PLUGIN_PATHS = ['./plugins/pelican-plugins']
# LIQUID_TAGS = ["literal", "video", "include_code"]
LIQUID_CONFIGS = (("IGNORE_FILES", ".ipynb_checkpoints", ""), ("CODE_DIR", "features/code", ""), ("NOTEBOOK_DIR", "features/notebooks", "")
) #

ENABLE_MATHJAX = True # testing this
EXTRA_HEADER = open('_nb_header.html', encoding='utf-8').read()

# Setting up extra pages
ABOUT_PAGE = '/pages/about.html'
GITHUB_USERNAME = 'blademaw'
LINKED_IN = 'https://www.linkedin.com/in/jack-roy-oliver/'
GOODREADS = 'https://www.goodreads.com/user/show/104565077-jack-oliver'
AUTHOR_BLOG = 'http://blademaw.github.io'
# AUTHOR_CV = "https://docs.google.com/viewer?url=https://github.com/blademaw/cv/raw/main/resume.pdf"
AUTHOR_CV = '/features/files/cv.pdf'

SHOW_ARCHIVES = True
SHOW_FEED = False  # Need to address large feeds

STATIC_PATHS = ['images', 'features', 'favicon.ico']

# Comments
DISQUS_SITENAME = 'blademaw-blog'

# License
# LICENSE_URL = "https://github.com/jakevdp/jakevdp.github.io-source/blob/master/LICENSE"
# LICENSE = "MIT"