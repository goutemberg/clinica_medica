from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&3d@0w2x0^@2juw_v478r0h_4rk6)iv_*o6r&hc0#eq!)th3&y'

DEBUG = True

ALLOWED_HOSTS = ['https://clinica-medica-i66x.onrender.com','localhost', '127.0.0.1','clinica-medica-i66x.onrender.com','0.0.0.0']

CSRF_TRUSTED_ORIGINS = ['https://clinica-medica-i66x.onrender.com','clinica-medica-i66x.onrender.com']


# Application definition

INSTALLED_APPS = [
    'home',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'plantao_pro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'home', 'templates/plantaopro/pages')],
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

WSGI_APPLICATION = 'plantao_pro.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'banco.sqlite3'),
    }
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': os.getenv('POSTGRES_DB'),
#        'USER': os.getenv('POSTGRES_USER'),
#        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
#        'HOST': os.getenv('POSTGRES_HOST'),
#        'PORT': os.getenv('POSTGRES_PORT'),
#    }
#}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'mgl_base_dados',
#        'USER': 'usuario_mgl',
#        'PASSWORD': 'McqAdGu54NougOKPqxHvPjTNVUgYD8XI',  
#        'HOST': 'dpg-crutsju8ii6s738hnki0-a',
#        'PORT': '5432',
#        'CONN_MAX_AGE': 600,  # Conexões persistentes com o banco de dados
#    }
#}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Em produção (quando DEBUG é False), o Django coleta todos os arquivos estáticos aqui
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Diretório para salvar arquivos de mídia (uploads de usuários)
MEDIA_ROOT = os.path.join(BASE_DIR, '/data/web/media')

# Para permitir que o WhiteNoise sirva arquivos estáticos de forma otimizada
if not DEBUG:
    #STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Configurações adicionais de arquivo estático
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, './home/static/plantaopro'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
