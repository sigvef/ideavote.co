import os

DEBUG = True

APPEND_SLASH = False

SESSION_COOKIE_DOMAIN = 'localhost'

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

SECRET_KEY = 'llk5is+*3p4!9x)nioo#dj2y6ndg-xca8ndzu*b5@hkd-k+irn'

ALLOWED_HOSTS = ['ideavote.co', '.ideavote.co']

INSTALLED_APPS = [
    'ideax',
    'ideax.comment',
    'ideax.frontpage',
    'ideax.idea',
    'ideax.notify',
    'ideax.site',
    'ideax.user',

    'anymail',
    'mptt',
    'social.apps.django_app.default',
    'taggit',

    'django.contrib.admin',
    'registration',  # should be immediately above django.contrib.auth
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',

    'notifications',  # needs to come after apps that generate notifications
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'ideax.middleware.CurrentSiteMiddleware',
]

ROOT_URLCONF = 'ideax.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates',
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
                'ideax.context_processors.google_analytics',
            ],
        },
    },
]

WSGI_APPLICATION = 'ideax.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.'
        'UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = False

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'ideax/static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

TAGGIT_CASE_INSENSITIVE = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGIN_REDIRECT_URL = '/'

ANYMAIL = {}
DEFAULT_FROM_EMAIL = 'noreply@mg.ideavote.co'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(levelname)s %(asctime)s %(module)s '
                       '%(process)d %(thread)d %(message)s')
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'log_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'django.log'),
            'maxBytes': '16777216',  # 16megabytes
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        '': {
            'handlers': ['log_file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

AUTHENTICATION_BACKENDS = (
    'social.backends.reddit.RedditOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_REDDIT_KEY = ''
SOCIAL_AUTH_REDDIT_SECRET = ''
SOCIAL_AUTH_REDDIT_AUTH_EXTRA_ARGUMENTS = {'duration': 'permanent'}

GOOGLE_ANALYTICS_KEY = ''
