"""
A variation on the local environment that uses mysql for the analytics database.

Useful for developers running both mysql ingress locally and the api locally
"""


from analyticsdataserver.settings.local import *

########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'analytics-api',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '172.18.0.4',# docker inspect edx.devstack-juniper.master.mysql | grep -e "IPAddress"
        'PORT': '3306',
    },
    'analytics': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'reports',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '172.18.0.4',# docker inspect edx.devstack-juniper.master.mysql | grep -e "IPAddress"
        'PORT': '3306',
    },
}
