import os
from pathlib import Path

from django.urls import reverse

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = "io^6bl^y5x-%-@0@78h=%-7d@g&nhj0kf1n&o29ti6w&1-0iy_"

DEBUG = True

ALLOWED_HOSTS = ["yourdomain.com", "127.0.0.1", "localhost"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "store",
    "basket",
    "account",
    "orders",
    "mptt",
    "core",
    "checkout",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "store.context_processors.categories",
                "basket.context_processors.basket",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = "/static/"

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

# Basket session ID
BASKET_SESSION_ID = "basket"


# Custom user model
AUTH_USER_MODEL = "account.Customer"
LOGIN_REDIRECT_URL = "/account/dashboard"
LOGIN_URL = "/account/login/"


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Stripe Payment
PUBLISHABLE_KEY = (
    "pk_test_51Iue40Jq5DvIQUocXhpe8yXeANvVlFmDR6ZQhDWpyVOhsBJR32ikAEJK6wQMWsYSffDc6ztoqFmvicxgGx1fOK1G00ZByYpSgW"
)
SECRET_KEY = (
    "sk_test_51Iue40Jq5DvIQUocS0yulXMtDorN6MKLlBLjYCWsnDaDk9JZkoo8c5OZB8rWpe2vWORYPCcLo45GchK0yM6r17df009EfLqHaf"
)
STRIPE_ENDPOINT_SECRET = "whsec_3vrLVwRwy582LdH6v3ovsMX8msfRcejx"
