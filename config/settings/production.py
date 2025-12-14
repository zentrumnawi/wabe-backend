import logging
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .common import *  # noqa

# SECRET CONFIGURATION
SECRET_KEY = env('DJANGO_SECRET_KEY')

# SECURITY CONFIGURATION
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    'DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS', default=True
)
SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    'DJANGO_SECURE_CONTENT_TYPE_NOSNIFF', default=True
)
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SECURE_SSL_REDIRECT = env.bool('DJANGO_SECURE_SSL_REDIRECT', default=True)
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'

# PRODUCTION MIDDLEWARE
WHITENOISE_MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
MIDDLEWARE = WHITENOISE_MIDDLEWARE + MIDDLEWARE

# STATICFILES
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ALLOWED HOSTS
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')

# URL that handles the media served from MEDIA_ROOT, used for managing
# stored files.
MEDIA_URL = env("DJANGO_CDN_URL")

# APPS
INSTALLED_APPS += ("gunicorn", )

# DATABASE
DATABASES = {'default': env.db("DATABASE_URL")}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# EMAIL
EMAIL_HOST = env("DJANGO_EMAIL_HOST", default=None)
EMAIL_PORT = 25
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
SYSTEM_EMAIL = env("SYSTEM_EMAIL")

# Sentry Configuration
SENTRY_DSN = env('DJANGO_SENTRY_DSN')

sentry_sdk.init(
    dsn=SENTRY_DSN, integrations=[DjangoIntegration()], send_default_pii=True
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {'level': 'WARNING', 'handlers': ['console']},
    'formatters': {
        'verbose': {
            'format':
            '%(levelname)s %(asctime)s %(module)s '
            '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'django.security.DisallowedHost': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}

# ADMIN URL
ADMIN_URL = env('DJANGO_ADMIN_URL')

# Static
STATIC_URL = "https://{}/{}static/".format(ALLOWED_HOSTS[0], URI_PREFIX)
