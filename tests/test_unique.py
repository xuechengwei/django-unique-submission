#!/usr/bin/env python

import sys
import os

test_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(test_dir, os.path.pardir))
os.environ['DJANGO_SETTINGS_MODULE'] = 'test_settings'


from django.test import simple
from django.test.client import Client
from django.core.management import call_command
from django_unique_submission.middlewares import UniqueSubmissionMiddleware

class UniqueSubmissionTestSuite(object):

    def setUp(self):
        self.runner = simple.DjangoTestSuiteRunner()
        self.config = self.runner.setup_test_environment()
        self.client = Client()

    def  
