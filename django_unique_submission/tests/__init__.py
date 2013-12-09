import json

from django.test import TestCase
from django.test.client import Client

class UniqueTestCase(TestCase):

    def setUp(self):

        self.c = Client()

    def test_token_generate(self):
        result = json.loads(self.c.get('/echo/').content)
        self.assertEquals(len(result['unique_token']), 48)

    def test_token_validation(self):

        result = json.loads(self.c.get('/echo/').content)

        tok = result['unique_token']

        fetch = json.loads(self.c.post('/echo/', {'unique_token':tok}).content)

        self.assertEqual(fetch['method'],'POST')

    def test_token_lock(self):
        
        import os
        utok = os.urandom(24).encode('hex').strip()
        fetch = self.c.post('/echo/', {'unique_token':utok})
        # can't be the same!!
        self.assertEqual(fetch.status_code,409)


    def test_token_checkitem(self):
        
        fetch = self.c.post('/echo/')

        self.assertEqual(fetch.status_code,412)
