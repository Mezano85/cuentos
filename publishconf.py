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
AUTHOR_INTRO = u'Soy Francisco G. Mezano, un visionario en el campo de los datos con una pasión por impulsar el valor empresarial a través de la innovación data-driven. Mi experiencia en data engineering, DataOps y data science me ha permitido liderar equipos y proyectos que transforman la manera en que las organizaciones aprovechan sus datos para la toma de decisiones estratégicas.   '
AUTHOR_DESCRIPTION = u'Estadístico | Data Scientist | Data Analyst | Data Engineer | Data Team Lead | DataOps Manager'
AUTHOR_AVATAR = 'https://elhogardelbuho.com/assets/img/profile-img.jpg'
AUTHOR_WEB = 'https://elhogardelbuho.com/'

# Services
GOOGLE_TAG = 'G-KHB57NQZEG'
#DISQUS_SITENAME = 'johndoe'

# Social
SOCIAL = (
   # ('facebook', 'http://www.facebook.com/johndoe'),
    ('x-twitter', 'https://twitter.com/FranciscoM76995'),
    ('github', 'https://github.com/mezano85'),
    ('linkedin', 'http://www.linkedin.com/in/mezano'),
)

DISPLAY_CATEGORIES_ON_MENU = False

# Menu
MENUITEMS = (
    ('Cuentos', f'{CATEGORIES_SAVE_AS}'),
    #('Archive', f'{ARCHIVES_SAVE_AS}'),
)
