AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
KEY_NAME = ''

ADMINS = (('', ''),)

ALLOWED_HOSTS = ['']

SECRET_KEY = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mindlogs',
        'USER': 'mindlogger',
        'PASSWORD': 'mindlogger',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

# email configuration
EMAIL_USE_TLS = True
EMAIL_HOST = ''
EMAIL_PORT = 465
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = ''
SERVER_EMAIL = ''

# Social Auth
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''