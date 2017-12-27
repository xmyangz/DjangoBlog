"""
Django settings for DjangoBlog project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
import sys
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = False
TESTING = len(sys.argv) > 1 and sys.argv[1] == 'test'

# ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    # 第三方应用程序 
    'bootstrap3',
    'xadmin',
    'crispy_forms',
    'reversion',

    #'pagedown',
    'markdownx',
    'haystack',
    'blog',
    'accounts',
    'comments',
    'oauth',
    'servermanager',
    'compressor',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'blog.middleware.OnlineMiddleware'
]

ROOT_URLCONF = 'DjangoBlog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'blog.context_processors.seo_processor'
            ],
        },
    },
]

WSGI_APPLICATION = 'DjangoBlog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases


DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #'ENGINE': 'django.db.backends.mysql',
        #'NAME': 'djangoblog',
        #'USER': os.environ.get('DJANGO_MYSQL_USER'),
        #'PASSWORD': os.environ.get('DJANGO_MYSQL_PASSWORD'),
        #'HOST': os.environ.get('DJANGO_MYSQL_HOST'),
        #'PORT': 3306,
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangoblog',
        'USER': 'postgres',
        'PASSWORD': os.environ.get('POSTGRESQL_PASSWORD'),
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/


SITE_ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = os.path.abspath(os.path.join(SITE_ROOT, '../'))


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'DjangoBlog.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}
# 自动更新搜索索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
# 允许使用用户名或密码登录
AUTHENTICATION_BACKENDS = ['accounts.user_login_backend.EmailOrUsernameModelBackend']

STATIC_ROOT = os.path.join(SITE_ROOT, 'collectedstatic')
STATIC_URL = '/static/'
STATICFILES = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(SITE_ROOT, 'static/media')
MEDIA_URL = '/static//media/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(SITE_ROOT, 'static/media'),
)

#MarkdownX 设置
MARKDOWNX_UPLOAD_CONTENT_TYPES = 'image/jpeg', 'image/png', 'image/svg+xml', 'image/gif'
MARKDOWNX_MEDIA_PATH = 'uploads/blog/images'
MARKDOWNX_UPLOAD_MAX_SIZE = 5 * 1024 * 1024
#MARKDOWNX_IMAGE_MAX_SIZE = _mdx('IMAGE_MAX_SIZE', dict(size=(IM_WIDTH, IM_HEIGHT), quality=NINETY_DPI))
#MARKDOWNX_SVG_JAVASCRIPT_PROTECTION = True

AUTH_USER_MODEL = 'accounts.BlogUser'
LOGIN_URL = '/login/'

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
DATE_TIME_FORMAT = '%Y-%m-%d'

SITE_NAME = '羊村笔记本'
SITE_DESCRIPTION = '知识是人类进步的阶梯。'
SITE_SEO_DESCRIPTION = '本站主要用来分享和记录学习经验、教程，以及一些随笔。欢迎大家访问！'
SITE_SEO_KEYWORDS = 'linux,windows,mac,mysql,mssql,postgresql,web,delphi,fmx,prolog,python,django,爬虫,大数据,人工智能'

ARTICLE_SUB_LENGTH = 300
SHOW_GOOGLE_ADSENSE = False
# bootstrap颜色样式
BOOTSTRAP_COLOR_TYPES = [
    'default', 'primary', 'success', 'info', 'warning', 'danger'
]

# 侧边栏文章数目
SIDEBAR_ARTICLE_COUNT = 10
# 侧边栏评论数目
SIDEBAR_COMMENT_COUNT = 5

# 分页
PAGINATE_BY = 10
# http缓存时间
CACHE_CONTROL_MAX_AGE = 2592000
# cache setting

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'TIMEOUT': 10800,
        'LOCATION': '127.0.0.1:11211',
    },
    'locmemcache': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'TIMEOUT': 10800,
        'LOCATION': 'unique-snowflake',
    }
}
CACHE_MIDDLEWARE_SECONDS = 60 * 60 * 10
CACHE_MIDDLEWARE_KEY_PREFIX = "djangoblog"
CACHE_MIDDLEWARE_ALIAS = 'default'

# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# SESSION_CACHE_ALIAS = 'default'

# Emial:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = True
# EMAIL_USE_SSL = True

EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'yyxfans@163.com'
EMAIL_HOST_PASSWORD = os.environ.get('MAIL_PASSWORD')
SERVER_EMAIL = 'xmyangz@qq.com'
DEFAULT_FROM_EMAIL = SERVER_EMAIL
# 设置debug=false 未处理异常邮件通知
ADMINS = [('xmyangz', 'xmyangz@qq.com')]
# 微信管理员密码(两次md5获得)
WXADMIN = 'a0455106316af45a76f2cf037522780d'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'log_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'djangoblog.log',
            'maxBytes': 16777216,  # 16 MB
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'null': {
            'class': 'logging.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'djangoblog': {
            'handlers': ['log_file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other
    'compressor.finders.CompressorFinder',
)
COMPRESS_ENABLED = True
# COMPRESS_OFFLINE = True


COMPRESS_CSS_FILTERS = [
    # creates absolute urls from relative ones
    'compressor.filters.css_default.CssAbsoluteFilter',
    # css minimizer
    'compressor.filters.cssmin.CSSMinFilter'
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter'
]

# Heroku设置

# 让request.is_secure()承认X-Forwarded-Proto头
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

if os.getcwd() == '/app': # Heroku设置
    import dj_database_url
    DATABASES = { 
        'default': dj_database_url.config(default='postgres://localhost')
        }

    # 只允许Heroku托管这个项目
    #ALLOWED_HOSTS = ['yangz.herokuapp.com']
    ALLOWED_HOSTS = ['blog.easysoft.club', 'yangz.herokuapp.com']
    SITE_URL = 'http://blog.easysoft.club'
    DEBUG = False
elif sys.platform == 'linux': #京东云服务器
    #ALLOWED_HOSTS = ['blog.easysoft.club']
    ALLOWED_HOSTS = ['*']
    SITE_URL = 'http://116.196.102.151' #'https://blog.easysoft.club'
    DEBUG = False
elif sys.platform == 'darwin': #mac本机
    ALLOWED_HOSTS = ['*']
    DEBUG = True
    DEBUG_PROPAGATE_EXCEPTIONS = True
    SITE_URL = 'http://localhost'    


OAHUTH = {
    'sina': {
        'appkey': os.environ.get('SINA_APP_KEY'),
        'appsecret': os.environ.get('SINA_APP_SECRET'),
        'callbackurl': SITE_URL+'/oauth/authorize?type=weibo'
    },
    'google': {
        'appkey': os.environ.get('GOOGLE_APP_KEY'),
        'appsecret': os.environ.get('GOOGLE_APP_SECRET'),
        'callbackurl': SITE_URL+'/oauth/authorize?type=google'
    },
    'github': {
        'appkey': os.environ.get('GITHUB_APP_KEY'),
        'appsecret': os.environ.get('GITHUB_APP_SECRET'),
        'callbackurl': SITE_URL+'/oauth/authorize?type=github'
    },
    'facebook': {
        'appkey': os.environ.get('FACEBOOK_APP_KEY'),
        'appsecret': os.environ.get('FACEBOOK_APP_SECRET'),
        'callbackurl': SITE_URL+'/oauth/authorize?type=facebook'
    }
}

SITE_ID = 1
BAIDU_NOTIFY_URL = "http://data.zz.baidu.com/urls?site=http://blog.easysoft.club&token=bda8aKdHp58MYeOk"

