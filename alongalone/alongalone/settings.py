"""
얼롱얼롱 프로젝트 app 목록:
    1. alongapp : 메인화면(base.html포함) 및 지도탭
    2. accountapp : 계정관련기능
    3. communityapp : 게시판탭(여기에 모든 혼카테고리 포함)
    4. commentapp : 게시판탭의 댓글기능(필요시, commentapp 을 comminityapp에 병합할 수도)
    5. filterapp : 미정(현재 안쓰임)
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d&36s%rwi(f7henc%ezn3_cv04po9bdpghw9xjp+!m6pwr++)6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition
# 외부 어플(pip install ~)은 ""로 표현했다.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'alongapp',
    'commentapp',
    'accountapp',
    'communityapp',
    "imagekit",
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

ROOT_URLCONF = 'alongalone.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            #base.html의 위치
            #base.html은 모든 앱마다의 templates에 상속해줘야하니,
            #프로젝트 상위폴더에 templates/base.html을 놓을 것임.
            #아래는 위가 가능하게 해주는 코드
            BASE_DIR / "templates"
        ],
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

WSGI_APPLICATION = 'alongalone.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#기본 유저 모델을 우리가 커스텀한 모델로 지정
AUTH_USER_MODEL = "accountapp.User"

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

#웹 내부 데이터는 두가지로 분류된다.
#하나는 static.
#이는 웹 내부에 이미 저장되어있는 데이터를 말한다.
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
#STAICFILES_DIR은 static파일들의 경로이다.
STATICFILES_DIRS =[
    BASE_DIR / "static",
]

#STATIC_URL은 static파일들을 제공할 URL이다.
STATIC_URL = 'static/'

#STATIC_ROOT는 static파일들을 복사하여 모아 놓을 경로이다.
#이게 필요한 이유는, DEBUG가 True일땐 runserver커맨드만으로도 브라우저에서 자동으로 static파일들을 모아놔주지만
#배포를 할땐 DEBUG를 반드시 False로 해야한다. 그래서 배포전 static파일들을 한데 모아놔야한다. 그 모으는 장소가 STATIC_ROOT이다.
#터미널에 "python manage.py collectstatic"으로 모아놓을수 있다.
#윗줄의 커맨드의 결과론 항상 staticfiles란 폴더가 생기고 거기에 모아지니 STATIC_ROOT를 아래와같이 설정해야한다.
STATIC_ROOT = os.path.join("staticfiles")

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

MEDIA_URL = "/media/"