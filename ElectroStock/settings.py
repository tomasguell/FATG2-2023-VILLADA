"""
Django settings for ElectroStock project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
from datetime import timedelta
from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-ff=y)c_ri$c_l3)#zz#%)8&gffn85+^5vo)+enx*6t1jov8*ok"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', 'electrostock-dev.fl0.io']
CSRF_TRUSTED_ORIGINS = ['https://electrostock-dev.fl0.io','https://*.127.0.0.1','https://electrostock-dev.fl0.io','https://*.mydomain.com','https://*.127.0.0.1','http://127.0.0.1:3000']


# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "ElectroStockApp",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "api.apps.ApiConfig",
    "coreapi",
    'corsheaders',
    'import_export',
    "rest_framework",
    "LoginApp",
    "notifications",
    'rest_framework_simplejwt.token_blacklist',
    "channels",
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
FRONTEND_URL = 'http://localhost:3000'

ROOT_URLCONF = "ElectroStock.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "ElectroStock.wsgi.application"
ASGI_APPLICATION= "ElectroStock.asgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3"}
}

#aca le digo a django que use de usuario la clase personalizada
AUTH_USER_MODEL = 'ElectroStockApp.CustomUser'

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "es"

TIME_ZONE = "America/Cordoba"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/img-prod/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'img-prod')
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Villada",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Villada",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    #"site_brand": "Villada",

    # Logo to use for your site, must be present in static files, used for brand on top left
    #"site_logo": "",
    

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    #"login_logo": "",

    # Logo to use for login form in dark themes (defaults to login_logo)
    #"login_logo_dark": None,

    # CSS classes that are applied to the logo above
    #"site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    #"site_icon": "",

    # Welcome text on the login screen
    "welcome_sign": "BIENVENIDO ",

    # Copyright on the footer
    "copyright": "Scrumton",

    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],


    #aca van los de la navar
    "topmenu_links": [

        # external url that opens in a new window (Permissions can be added)
        {"name": "Tienda ", "url": "http://127.0.0.1:3000/tienda", "new_window": False},

        # external url that opens in a new window (Permissions can be added)
        {"name": "Presupuesto", "url": "http://127.0.0.1:3000/presupuesto", "new_window": False},

        # external url that opens in a new window (Permissions can be added)
        {"name": "Prestamo", "url": "http://127.0.0.1:3000/prestamo", "new_window": False},

        

    ],
    # Custom links to append to app groups, keyed on app name
    "custom_links": {
        "books": [{
            "name": "Make Messages", 
            "url": "make_messages", 
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "ElectroStockApp.Box":"fas fa-box",
        "ElectroStockApp.Location":"fas fa-map-marker-alt",
        "ElectroStockApp.CustomUser":"fas fa-user",
        "ElectroStockApp.Category":"fas fa-ellipsis-h",
        "ElectroStockApp.Element":"fas fa-hammer",
        "ElectroStockApp.Log":"fas fa-exchange-alt",
        "ElectroStockApp.Laboratory":"fas fa-flask",
        "ElectroStockApp.TokenSignup":"fas fa-user-secret",
        "ElectroStockApp.Speciality":"fas fa-hard-hat",
        "ElectroStockApp.Course":"fas fa-graduation-cap",
        "token_blacklist.blacklistedtoken":"fas fa-lock",
        "token_blacklist.outstandingtoken":"fas fa-lock",
    },

    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,

    "usermenu_links": [
        {"name": "Token", "url": "http://127.0.0.1:8000/admin/ElectroStockApp/tokensignup/", "new_window": False, "icon":"fas fa-user-secret",},
    ],
    
    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    
}
JAZZMIN_SETTINGS["show_ui_builder"] = True

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-info",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "litera",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": False
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}




SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=100000),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=50),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',

    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=100000),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}



CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1:3000',  # Agrega aquí tu URL de origen permitido
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',

]

# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST= 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'electrostock.noreplay@gmail.com'
EMAIL_HOST_PASSWORD = 'exjvovbiofvrbgej' #NO BORRAR ESTO NUNCA, also, Pepe1234
EMAIL_USE_TLS = True



# celery -A ElectroStock worker --beat --loglevel=info
# Redis configuration 
from datetime import timedelta

CELERY_BROKER_URL = CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672/'  # Ejemplo para RabbitMQ
CELERY_ACCEPT_CONTENT=['json']
CELERY_TASK_SERIALIZER= 'json'
CELERY_IMPORTS = ('ElectroStockApp.task',)
CELERY_BEAT_SCHEDULE = {
    'run_check_expired_logs': {
        'task': 'ElectroStockApp.task.run_check_expired_logs',
        'schedule': timedelta(days=1),  # Ejecutar cada 1 día
    },
    'assign_next_year_course': {
        'task': 'ElectroStockApp.task.assign_next_year_course',
        'schedule': timedelta(days=365),  # Ejecutar cada 1 año
    },
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',  # Puedes ajustar el nivel según tus necesidades
    },
}



CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}