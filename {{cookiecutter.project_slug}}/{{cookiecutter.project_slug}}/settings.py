import os

REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost')
REDIS_POOLSIZE = os.getenv('REDIS_URL', 10)
REDIS_TIMEOUT = os.getenv('REDIS_TIMEOUT', 60)

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
