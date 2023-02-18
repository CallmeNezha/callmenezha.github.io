AUTHOR = 'Zijian Jiang'
SITENAME = "Zijian Jiang's Journal"
SITEURL = 'https://callmenezha.github.io'

TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = 'en'

SUBTITLE = 'Hello World!'
SUBTEXT = '''
Hello, and welcome to my modest corner of the web!

This blog began in 2023 as a personal online journal, 
it mostly contains technical, programming-related posts. 
It's my way to document things I find interesting for my future self.

The contents of this blog reflect my personal opinions only; 
writing the posts and the programming explorations accompanying them are done in my free time. 
I never write on behalf of my employer in this blog. 
As a policy, it also doesn't contain paid writing assignments and I don't accept "guest posts" 
from others.

'''
COPYRIGHT = '©2023'
PATH = 'content'
THEME = 'themes/Papyrus'
OUTPUT_PATH = 'docs'
THEME_STATIC_PATHS = ['static']
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['readtime', 'neighbors', 'pelican-toc']

DISPLAY_PAGES_ON_MENU = True
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'about'))
PAGINATED_TEMPLATES = {'index':None,'tag':None,'category':None,'author':None,'archives':24,}

# Site search plugin
# SEARCH_MODE = "docs"
# SEARCH_HTML_SELECTOR = "main"
# Table of Content Plugin
TOC = {
    'TOC_HEADERS'       : '^h[1-3]', # What headers should be included in
                                     # the generated toc
                                     # Expected format is a regular expression
    'TOC_RUN'           : 'true',    # Default value for toc generation,
                                     # if it does not evaluate
                                     # to 'true' no toc will be generated
    'TOC_INCLUDE_TITLE': 'false',    # If 'true' include title in toc
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
RSS_FEED_SUMMARY_ONLY = None

# Social widgets
SOCIAL = (
    ('github', 'https://github.com/CallmeNezha'),
)

# Article share widgets
SHARE = (
    ("twitter", "https://twitter.com/intent/tweet/?text=Features&amp;url="),
    ("linkedin", "https://www.linkedin.com/sharing/share-offsite/?url="),
    ("reddit", "https://reddit.com/submit?url="),
    ("facebook", "https://facebook.com/sharer/sharer.php?u="),
    ("whatsapp", "https://api.whatsapp.com/send?text=Features - "),
    ("telegram", "https://telegram.me/share/url?text=Features&amp;url="),
)

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# DISQUS_SITENAME = ''
# GOOGLE_ANALYTICS = ''