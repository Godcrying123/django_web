from .base import * # NOQA

DEBUG = True

# ALLOWED_HOSTS = ['jackson.com']

DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.mysql',
      'NAME': 'myidea_db',
      'USER': 'root',
      'PASSWORD': 'iso*help',
      'HOST': '127.0.0.1',
      'PORT': '3306',
      'CONN_MAX_AGE': 5 * 60,
      'OPTIONS': {'charset': 'utf8mb4'},
    },
}

# MIDDLEWARE += [
#     'django.middleware.cache.UpdateCacheMiddleware',
# ]

REDIS_URL = 'redis://127.0.0.1:6379/1'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'TIMEOUT': 300,
        'OPTIONS': {
            'PASSWORD': 'iso*help',
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        },
        'CONNECTION_POOL_CLASS': 'redis.connection.BlockingConnectionPool',
    }
}
