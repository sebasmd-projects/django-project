import os
from unipath import Path

gettext = lambda s: s

DATA_DIR = os.path.dirname(os.path.dirname(__file__))

BASE_DIR = Path(__file__).ancestor(3)

DEBUG = True

ALLOWED_HOSTS = []

SECRET_KEY = ''

DATABASES = {
    'default': {
        'ENGINE': '', 
        'NAME': '', 
        'USER': '', 
        'PASSWORD': '', 
        'HOST': '', 
        'PORT': '', 
    } 
}

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages', 
)


LOCAL_APPS = (
    'app_core_cnt',
    'apps.page.about',
    'apps.page.blog',
    'apps.page.contact',
    'apps.page.index',
    'apps.page.resume',
    'apps.general.users',
    'apps.nlp.nlp_admin',
)

THIRD_PARTY_APPS = (
    'ckeditor',
    'sekizai',
    'treebeard',
    'filer',
    'easy_thumbnails',
    'fontawesome-free',
)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

AUTH_USER_MODEL = 'users.User'

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.child('cnt','templates'),],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'apps.page.index.context_processors.ctx_redes_sociales',
                'apps.page.index.context_processors.ctx_typing',
                'apps.page.index.context_processors.ctx_title',
                'apps.page.index.context_processors.ctx_app_name',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ],
        },
    },
]

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

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

ROOT_URLCONF = 'app_core_cnt.urls'

WSGI_APPLICATION = 'app_core_cnt.wsgi.application'

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Bogota'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEFAULT_CHARSET = 'utf-8'

X_FRAME_OPTIONS = 'SAMEORIGIN'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_DIRS = (
    BASE_DIR.child('cnt','static'),
)

MEDIA_ROOT = BASE_DIR.child('cnt', 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = BASE_DIR.child('cnt', 'staticfiles')
STATIC_URL = '/static/'

LANGUAGES = (
    ('es-co', gettext('Español Colombia')),
    ('en', gettext('English')),
)

LOCALE_PATHS = [
    BASE_DIR.child('cnt','locale'),
]

CKEDITOR_CONFIGS = {
    # Configuración para el CKEDITOR
    'default': {
        'removePlugins':'stylesheetparser',
        'skin': 'moono',
        'toolbar': 'full',
        'toolbarCanCollapse': True,
    },
}

CKEDITOR_UPLOAD_PATH = 'media/filer_public/ckeditor/uploads'
CKEDITOR_IMAGE_BACKEND = 'pillow'

# EMAIL SETTINGS

#Descomentar dependiendo del uso
#EMAIL_USE_SSL = True #Para utilizar el puerto 465 (seguro)
#EMAIL_USE_TLS = True #Para utilizar el puerto 587 (no seguro)

EMAIL_BACKEND = ''

EMAIL_HOST = '' 

EMAIL_PORT = ''

EMAIL_HOST_USER = '' 

EMAIL_HOST_PASSWORD = ''

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

print('=====================================')
print('     ____________   _____________')
print('   //         666\ /          667\\\ ')
print(' /|               |               |\ ')
print('|||      ==       |               |||')
print('|||   <^\()/^>    |     Juan      |||')
print('|||    \/  \/     |   Sebastian   |||')
print('|||     /  \      |    Morales    |||')
print('|||     `\'\'`      |               |||')
print('|||_____________  |  _____________|||')
print(' /_____/--------\\\_//--------\_____\ ')
print('Si puedes imaginarlo, puedes programarlo')
print('=====================================')
