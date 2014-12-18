#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kelsey Gilmore-Innis'
SITENAME = u'blog blog blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

THEME = "./themes/SoMA2"
MD_EXTENSIONS = ['codehilite(linenums = True)']
PLUGIN_PATHS = ['/Users/hbic/code/pelican-plugins']
PLUGINS = ['read_more_link', 'share_post']
LOAD_CONTENT_CACHE = False

SITESUBTITLE = "KGI"
SITETAGLINE = "blog blog blog"
DISQUS_SITENAME = "kelseynerd"
TWITTER_USERNAME = "kelseyinnis"

READ_MORE_LINK = '<span>Read more</span>'
READ_MORE_LINK_FORMAT = '<div class="navButton"><a href="/{url}">{text}</a></div>'

FEED_ALL_ATOM = 'feeds/all.atom.xml'

