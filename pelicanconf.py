#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Comunidade'
SITENAME = 'TecSorocabana'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'
LOCALE = 'pt_BR'
DEFAULT_LANG = 'pt-br'

# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'blog/feeds/all.rss.xml'
FEED_ALL_ATOM = 'blog/feeds/all.atom.xml'
FEED_MAX_ITEMS = 15
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'sitemap']
SITEMAP_SAVE_AS = 'sitemap.xml'

THEME = 'themes/pelican-alchemy/alchemy'

USE_FOLDER_AS_CATEGORY = True
DELETE_OUTPUT_DIRECTORY = True

DEFAULT_METADATA = {
    'description': 'Site da comunidade de tecnologia de Sorocaba',
}

ARTICLE_ORDER_BY = 'date'

ARCHIVES_SAVE_AS = 'blog_index.html'

PAGE_URL = PAGE_SAVE_AS = '{slug}.html'

SLUGIFY_SOURCE = 'basename'

LOAD_CONTENT_CACHE = False
CACHE_CONTENT = False

# Theme specific settings
ICONS = (
    ('slack', 'http://bit.ly/slack-tecsorocabana'),
    ('github', 'https://github.com/tecsorocabana'),
)

SITEIMAGE = 'https://i.imgur.com/3w1tsPS.png'
SITESUBTITLE = 'Comunidade de profissionais de tecnologia de Sorocaba'
DESCRIPTION = 'TecSorocabana é a comunidade de profissionais de tecnologia de Sorocaba'
HIDE_AUTHORS = True
