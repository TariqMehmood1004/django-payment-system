import os
from pathlib import Path



# ------------------------ Django settings ------------------------ #
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-vrg&i0cgyl8#--y(i_m!4a3u5bzqu!6gk=d9z0a$e)m5jslf%6'

API_NINJA_KEY = 'R58oMarCHAImxuwmSiwEkg==aLkR5NRWh5i7sE5B'
API_NINJA_BASE_URL = 'https://api.api-ninjas.com/v1'

HOST = 'http://127.0.0.1:8000'

STRIPE_SECRET_KEY='sk_test_51OotJiGRAnpadYao1PNTmn60XNIGSJmo7UpOjsrUQBvR7uhf5SKWVtQ4WFxJx1wprgL4IU3CHu6azMX6ifhpNk1R00bx30oDGU'
STRIPE_Publishable_key='pk_test_51OotJiGRAnpadYaoYuelpWhvwrZxoxetfFYnoI2fUy3B5cG2nxMC8ziwtPkWEldVBom9QVwhBMDQx4GldmP67Bgi0069akU3Fb'

DEBUG = True
ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'paymentSystemApp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'paymentSystemProject.urls'

TEMPLATES_DIR = BASE_DIR / 'templates'

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

WSGI_APPLICATION = 'paymentSystemProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static',]

# This production code might break development mode, so we check whether we're in DEBUG mode
if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# ------------------------ Email settings ------------------------ #
# Email settings - CREDENTIALS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.office365.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'TariqMehmood@thedarkbytes.com'  # Your Outlook email
EMAIL_HOST_PASSWORD = 'Y@611026051774uq'  # Your Outlook email password or app password
DEFAULT_FROM_EMAIL = 'TariqMehmood@thedarkbytes.com'  # Default sender email
ADMIN_DEFAULT_FROM_EMAIL = 'info@thedarkbytes.com'


