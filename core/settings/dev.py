from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "*9fs0asd93245opfs90)(45rohfrrvxi^k9%56(6c((lsuf3p^%3ami^@d^oa8oysk+1"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = [
        "ryanbradon.work",
        "127.0.0.1",
        "143.198.246.159"
        ]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"



try:
    from .local import *
except ImportError:
    pass
