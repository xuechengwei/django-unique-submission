#!/usr/bin/env python
import sys
import os

parent = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, parent)

from django.conf import settings

if not settings.configured:
    settings_dict = dict(
        INSTALLED_APPS=(
            'django.contrib.sessions',
            'django_unique_submission',
            ),
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3"
                }
            },
        MIDDLEWARES = (
            'django.middleware.common.CommonMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware'
            ),
        ROOT_URLCONF = 'django_unique_submission.tests.urls'
        )

    settings.configure(**settings_dict)

def runtests():

    from django.test.simple import DjangoTestSuiteRunner
    dtsr = DjangoTestSuiteRunner(verbosity=1,
                                    interactive=True, 
                                    failfast=False)
    failures = dtsr.run_tests(['django_unique_submission'])
    sys.exit(failures)

if __name__ == '__main__':
    runtests()
