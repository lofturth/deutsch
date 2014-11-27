"""
Django settings for deutsch project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

from .secret_key import SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


LOGIN_URL = '/login/'

LOGOUT_URL = '/logout/'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'quizzes',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'deutsch.middleware.RequireLoginMiddleware',
)

LOGIN_REQUIRED_URLS = (
    r'/(.*)$',  # TODO interpret this regex.
)
LOGIN_REQUIRED_URLS_EXCEPTIONS = (
    r'/login(.*)$',
    r'/logout(.*)$',
    r'/staff(.*)$',
)

ROOT_URLCONF = 'deutsch.urls'

WSGI_APPLICATION = 'deutsch.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates')
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

##STATICFILES_FINDERS = (
##    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
##    'django.contrib.staticfiles.finders.FileSystemFinder',
##)

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static_root')


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static', 'static_dirs'),

)

MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')

MEDIA_URL = '/media/'