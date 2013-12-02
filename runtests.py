#!/usr/bin/env python

from django.conf import settings

if not settings.configured:
    settings.configure( INSTALLED_APPS=tuple('django_unique_submission', ),
                       DEBUG=True,
                       SITE_ID=1)


if __name__ == '__main__':
    import sys
    import os
    root_dir = os.path.dirname(__file__)
    test_dir = os.path.join(root_dir, 'test')
    sys.path.append(test_dir)
    
    from django.test.simple import DjangoTestSuiteRunner
    test_runner = DjangoTestSuiteRunner()

    failures = test_runner.run_tests(['django_unique_submission',], verbosity=1)
    if failures:
            sys.exit(failures)
