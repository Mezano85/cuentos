from datetime import date

AUTHOR = 'Francisco G. Mezano'
SITENAME = 'DataOps Blog'
SITEPATH = ''
SITEURL = ''


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

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'theme/mezano'


# Theme customizations
#MINIMALXY_CUSTOM_CSS = 'static/custom.css'
MINIMALXY_FAVICON = 'favicon.ico'
MINIMALXY_START_YEAR = 2022
MINIMALXY_CURRENT_YEAR = date.today().year

# Author
AUTHOR_INTRO = u'Soy Francisco G. Mezano, un visionario en el campo de los datos con una pasión por impulsar el valor empresarial a través de la innovación data-driven. Mi experiencia en data engineering, DataOps y data science me ha permitido liderar equipos y proyectos que transforman la manera en que las organizaciones aprovechan sus datos para la toma de decisiones estratégicas.   '
AUTHOR_DESCRIPTION = u'Estadístico | Data Scientis | Data Analyst | Data Engineer | Data Team Lead | DataOps Manager'
AUTHOR_AVATAR = 'https://mezano85.github.io/assets/img/profile-img.jpg'
AUTHOR_WEB = 'https://mezano85.github.io/'

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
