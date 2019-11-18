#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import json
from collections import OrderedDict


AUTHOR = u'Fabien Leboeuf'
SITENAME = u'CGM2.i'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'English'


DELETE_OUTPUT_DIRECTORY = True

# BANNER
BANNER = 'images/bannerGait.png'
BANNER_SUBTITLE = 'Updating the Conventional Gait Model for the modern world'
BANNER_ALL_PAGES = True


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# link widget
LINKS = (('Salford Gait Analysis', 'http://www.salford.ac.uk/health-sciences/facilities/gait-analysis-clinic'),
        ('Vicon', 'https://www.vicon.com/'),
        ('ResearchGate Project page', 'https://www.researchgate.net/project/Conventional-Gait-Model-2'),
        ('Walking with Richard', 'https://wwrichard.net/'))

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)


PLUGIN_PATHS = ['plugins']
PLUGINS = ['bootstrap-rst','pelican-toc','pelican_youtube']
EXTENSIONS = ['toc']

#THEME = "C:/Users/AAA34169/Documents/Programming/webDevelopement/PelicanThemes/pelican-bootstrap3/"
THEME = "./Theme/boostrap3"
BOOTSTRAP_THEME = 'cosmo'
DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False


# MENU INFO
DISPLAY_RECENT_POSTS_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False
EXPAND_LATEST_ON_INDEX = False
USE_FOLDER_AS_CATEGORY = False

DISPLAY_RECENT_POSTS_ON_SIDEBAR     = True
# ARTICLE INFO
ARTICLE_PATHS = ['articles']
DEFAULT_DATE = 'fs'
PAGE_PATHS = ['pages']


# MENU with external json doc
MENU = json.loads(open(str('content/navbar.json')).read(),object_pairs_hook=OrderedDict)


#MENUITEMS = [('Team', '/pages/team.html'),
#             ('Installation', '/pages/installation.html'),
#             ('API Documentation', 'https://pycgm2.github.io/pyCGM2-API-DOC/index.html'),
#             ('cgm', '/index.html')]


STATIC_PATHS = [
    'html',"images","documentation","resources"
    ]


# url settings
ARTICLE_SAVE_AS = 'articles/{slug}.html'
ARTICLE_URL = 'articles/{slug}.html'
#ARTICLE_URL = 'articles/{slug}.html'
#ARTICLE_SAVE_AS = 'articles/{slug}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'
TAGS_URL = 'tags.html'

CC_LICENSE = "CC-BY"
CC_LICENSE_DERIVATIVES="yes"
CC_LICENSE_COMMERCIAL="yes"


SIDEBAR_IMAGES_HEADER = 'Main Sponsors'
SIDEBAR_IMAGES = ["/images/logo/vicon.jpg","/images/logo/salford.png"]

SIDEBAR_IMAGES_PARTNER_HEADER = 'Secondary Partners'
SIDEBAR_PARTNER_IMAGES = ["/images/logo/qualisys.png","/images/logo/trinoma.png"]

SIDEBAR_IMAGES_ACADEMICPARTNER_HEADER = 'Academic Partners'
SIDEBAR_ACADEMICPARTNER_IMAGES = ["/images/logo/unige.png"]


TOC = {
    'TOC_HEADERS'       : '^h[2-3]', # What headers should be included in
                                     # the generated toc
                                     # Expected format is a regular expression

    'TOC_RUN'           : 'true',    # Default value for toc generation,
                                     # if it does not evaluate
                                     # to 'true' no toc will be generated

    'TOC_INCLUDE_TITLE': 'true',     # If 'true' include title in toc
}
