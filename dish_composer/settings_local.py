# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dishes',
        'USER': 'dishmaker',
        'PASSWORD': 'aezakmi123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

CSRF_COOKIE_SECURE = False
