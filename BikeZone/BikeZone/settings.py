import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_DIR = os.path.join(BASE_DIR, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+ulgafz!=+2^91dovcfplq6z@aozpjjka$ubwvprb#+cr(6o_w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LOGIN_REDIRECT_URL = 'dashboard'


# Application definition

INSTALLED_APPS = [
    'material',
    'material.admin',
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bike_zone',
    'auth_app',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'ckeditor',

    # Providers
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google'
]

MATERIAL_ADMIN_SITE = {
    'HEADER':  ('BikeZone Administration'),  # Admin site header
    'TITLE':  ('BikeZone Administration'),  # Admin site title
    'FAVICON':  'bike_zone/img/icon-bike.ico',  # Admin site favicon (path to static should be specified)
    'MAIN_BG_COLOR':  'black',  # Admin site main color, css color should be specified
    'MAIN_HOVER_COLOR':  'red',  # Admin site main hover color, css color should be specified
    'PROFILE_PICTURE':  'bike_zone/img/avatar/avatar-mahin.jpg',  # Admin site profile picture (path to static should be specified)
    'PROFILE_BG':  'bike_zone/img/bike-3.jpg',  # Admin site profile background (path to static should be specified)
    'LOGIN_LOGO':  'bike_zone/img/avatar/avatar-mahin.jpg',  # Admin site logo on login page (path to static should be specified)
    'LOGOUT_BG':  'bike_zone/img/bike-2.jpg',  # Admin site background on login/logout pages (path to static should be specified)
    'SHOW_THEMES':  True,  #  Show default admin themes button
    'TRAY_REVERSE': True,  # Hide object-tools and additional-submit-line by default
    'SHOW_COUNTS': True, # Show instances counts for each model
    'APP_ICONS': { 'Tea_App' : 'apps', 'Accounts': 'email' },
}



# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'Portfolio_App',
#     'django_cleanup.apps.CleanupConfig',
  
    
    
# ]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'BikeZone.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'BikeZone.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# SMTP Config

# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'mahianmahin@yahoo.com'
# EMAIL_HOST_PASSWORD = 'zrdqhrdoliggklkc'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'anonymous.terminal13@gmail.com'
EMAIL_HOST_PASSWORD = 'wlieuccshhejbenr'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# STATIC_URL = '/static/'
# MEDIA_URL = '/images/'

# STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'static/images'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]




# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SITE_ID = 1