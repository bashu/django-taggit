from django.utils.translation import gettext_lazy as _

SECRET_KEY = "secretkey"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "taggit",
    "tests",
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

ROOT_URLCONF = "tests.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3"}}

SITE_ID = 1

LANGUAGE_CODE = "en-us"
LANGUAGES = (
    ("en-us", _("English")),
    ("fr", _("French")),
    ("es", _("Spanish")),
    ("it", _("Italian")),
    ("nl", _("Dutch")),
)

INSTALLED_APPS += ["parler"]  # noqa F405
PARLER_DEFAULT_LANGUAGE = LANGUAGE_CODE
PARLER_LANGUAGES = {
    SITE_ID: tuple([{"code": lang[0]} for lang in LANGUAGES]),
    "default": {"fallback": LANGUAGE_CODE, "hide_untranslated": False},
}
