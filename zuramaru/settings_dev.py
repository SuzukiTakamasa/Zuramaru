from .settings_common import *

#SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOST = []

#The setting of logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    #Logger
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },

        'mirazura': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },

        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'dev'
            },
        },

        'formatters': {
            'dev': {
                'format': '\t'.join([
                    '%(asctime)s',
                    '[%(levelname)s]',
                    '%(pathname)s(Line:%(lineo)d)',
                    '%(message)s%'
                ])
            },
        }
    }

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'