"""Devstack settings."""

from analyticsdataserver.settings.local import *

ALLOWED_HOSTS += ['edx.devstack.analyticsapi']

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

ELASTICSEARCH_LEARNERS_HOST = "edx.devstack.elasticsearch"
LMS_BASE_URL = "http://edx.devstack.lms:18000/"
