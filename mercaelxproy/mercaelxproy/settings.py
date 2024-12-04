"""
Django settings for mercaelxproy project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from django.contrib.messages import constants as messages


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hff2nlo%w1=+esj(dbeibyn126no%11z&xyy#3gr7onh51_l4c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ["localhost"]
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #-----UD6.2.f-----
    #Añadir las aplicaciones al proyecto
    'common',
    'core',
    'directorio_comercios',
    'anuncios',
    #-----UD7.4.b-----
    #Añadir crispy para usar bootstrap5
    'crispy_forms',
    'crispy_bootstrap5',

    #----UD8.1.a----
    #Añadir la aplicación de usuarios
    #'usuarios',
    #-----UD8.4-----
    #Añadir allauth para autenticación
    'django.contrib.sites', 
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #-----UD8.4-----
    #Añadir middleware de allauth
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'mercaelxproy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #-----UD6.2.e-UD6.2.g----
        #Añadido el directorio de templates
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'mercaelxproy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

#-----UD6.2.e-----
#Cambio de idioma y zona horaria
LANGUAGE_CODE = 'es'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

#-----UD6.2.e-----
#Añadido el directorio de media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'


#-----UD6.2.e-----
#Static_root añadido
STATIC_ROOT = os.path.join(BASE_DIR, 'static') # Añadir nueva

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#-----UD7.2.e-UD7.4.a-----
#Configuración de los mensajes de error para que se muestren con el estilo de bootstrap
MESSAGE_TAGS = {messages.ERROR: 'danger'}

#-----UD7.4.b-----
#Configuración de crispy para que use bootstrap5
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"


#----UD8.2.a-UD8.2.b----
#Redirección de login y logout
LOGIN_REDIRECT_URL = 'panel'
LOGOUT_REDIRECT_URL = 'home'


#----UD8.1.a-UD8.2.b----
#Añadir el modelo de usuario para que django lo use
# AUTH_USER_MODEL = 'usuarios.MyUser'


#----UD8.3----
#URL de login
#LOGIN_URL = 'login'


#-----UD8.4-----
# Configuración del sitio
SITE_ID = 1

#-----UD8.4-----
#Añadir autenticación de allauth
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

#-----UD8.4-----
#Configuración de Allauth
ACCOUNT_EMAIL_VERIFICATION = 'none'  #Desactivada la verificación por email
ACCOUNT_AUTHENTICATION_METHOD = 'email'  #Uso de email para autenticación
ACCOUNT_EMAIL_REQUIRED = True  #Email requerido para el registro
ACCOUNT_USERNAME_REQUIRED = False  #No requiere nombre de usuario
ACCOUNT_UNIQUE_EMAIL = True  #Email debe ser único

#-----UD8.5-----
# Configuración de Email para el envío de correos
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.gmx.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True 
EMAIL_HOST_USER = 'manuel6969@gmx.es' 
EMAIL_HOST_PASSWORD = 'LVIAJKFD5MNMJ4T64DKV'
DEFAULT_FROM_EMAIL = 'manuel6969@gmx.es'