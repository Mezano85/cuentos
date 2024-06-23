from datetime import date

AUTHOR = 'Francisco G. Mezano'
SITENAME = 'Los cuentos de Alondra'
SITEPATH = 'cuentos'
SITEURL = f'https://elhogardelbuho.com/{SITEPATH}'


PATH = 'content'

TIMEZONE = 'America/Mexico_City'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

CATEGORIES_SAVE_AS = 'categories.html'
ARCHIVES_SAVE_AS = 'archives.html'

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'theme/mezano'


# Theme customizations
#MINIMALXY_CUSTOM_CSS = 'static/custom.css'
MINIMALXY_FAVICON = 'favicon.ico'
MINIMALXY_START_YEAR = 2023
MINIMALXY_CURRENT_YEAR = date.today().year

# Author
AUTHOR_INTRO = u'Alondra es una pequeña de 4 años y estudiante de preescolar, llena de creatividad y energía. Cada noche, su imaginación la lleva a mundos llenos de fantasía y aventuras, creando cuentos que reflejan su curiosidad. Además de su pasión por los cuentos, Alondra disfruta inmensamente de la música y el baile, siempre moviéndose al ritmo de una melodía.'
# AUTHOR_DESCRIPTION = u'Estadístico | Data Scientist | Data Analyst | Data Engineer | Data Team Lead | DataOps Manager'
AUTHOR_AVATAR = '/theme/images/Alondra.jpeg'
# AUTHOR_WEB = '#'

# Services
GOOGLE_TAG = 'G-KHB57NQZEG'
#DISQUS_SITENAME = 'johndoe'

# Social
# SOCIAL = (
   # ('facebook', 'http://www.facebook.com/johndoe'),
#    ('x-twitter', 'https://twitter.com/FranciscoM76995'),
#    ('github', 'https://github.com/mezano85'),
#    ('linkedin', 'http://www.linkedin.com/in/mezano'),
#)

DISPLAY_CATEGORIES_ON_MENU = False

# Menu
MENUITEMS = (
    ('Cuentos', f'{CATEGORIES_SAVE_AS}'),
    #('Archive', f'{ARCHIVES_SAVE_AS}'),
)
