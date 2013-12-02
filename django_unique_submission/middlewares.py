"""
Unique Submission Middleware
Author: Meng Zhuo <mengzhuo1203@gmail.com>
If enable, each POST/PUT request will be convert into hash code and save into cache.

Setting Example::python

    MIDDLEWARE_CLASSES = [
        'django_unique_submission.UniqueSubmissionMiddleware',
        ...
    ]
"""
from django.conf import settings
from django.core.cache import get_cache
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _

from .unique_utils import make_cache_key

class UniqueSubmissionMiddleware(object):
    """
    Unique Submission Middleware
    """
    def __init__(self):
        self.cache_timeout = getattr(settings, 'UNIQUE_MIDDLEWARE_SECONDS', 10)
        self.key_prefix = getattr(settings, 'UNIQUE_MIDDLEWARE_KEY_PREFIX', 
                                 'umkp_')
        self.cache_alias = getattr(settings, 'UNIQUE_MIDDLEWARE_ALIAS', 'default')
        self.cache = get_cache(self.cache_alias)
        self.handle_methods = getattr(settings, 
                                        'UNIQUE_MIDDLEWARE_HANDLE_METHODS',
                                        ('POST', 'PUT'))

    def process_request(self, request):
        
        if not request.method in self.handle_methods:
            request._unique_request_handled = False
            return None
        
        request._unique_request_handled = True
        cache_key = make_cache_key(request, self.key_prefix, 
                                  request.method)
        if self.cache.get(cache_key):
            return HttpResponse(_('Request Conflicted'), status=409)
        else:
            self.cache.set(cache_key, cache_key, self.cache_timeout)
