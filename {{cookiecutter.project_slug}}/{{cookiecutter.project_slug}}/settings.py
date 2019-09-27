import os

REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost')
REDIS_DB = os.getenv('REDIS_DB', 0)
REDIS_POOLSIZE = os.getenv('REDIS_POOLSIZE', 10)
REDIS_TIMEOUT = os.getenv('REDIS_TIMEOUT', 60)

CACHE_URL = os.getenv('CACHE_URL', os.getenv('REDIS_URL', 'redis://localhost'))
CACHE_DB = os.getenv('CACHE_DB', 1)
CACHE_POOLSIZE = os.getenv('CACHE_POOLSIZE', 10)

LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] [%(process)d] [%(levelname)s] %(name)s:%(lineno)d - %(message)s'  # noqa
        },
        'simple': {
            'format': '%(levelname)s %(name)s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'asyncio': {
            'level': 'WARNING',
            'propagate': True,
        },
        'asyncio_redis': {
            'level': 'WARNING',
            'propagate': True,
        },
    }
}
