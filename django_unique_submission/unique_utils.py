import hashlib

from django.conf import settings
from django.utils.encoding import iri_to_uri, force_bytes, force_text
from django.utils.timezone import get_current_timezone_name
from django.utils.translation import get_language

# functions port from Django

def _i18n_cache_key_suffix(request, cache_key):
    """If necessary, adds the current locale or time zone to the cache key."""
    if settings.USE_I18N or settings.USE_L10N:
        # first check if LocaleMiddleware or another middleware added
        # LANGUAGE_CODE to request, then fall back to the active language
        # which in turn can also fall back to settings.LANGUAGE_CODE
        cache_key += '.%s' % getattr(request, 'LANGUAGE_CODE', get_language())
    if settings.USE_TZ:
        # The datetime module doesn't restrict the output of tzname().
        # Windows is known to use non-standard, locale-dependant names.
        # User-defined tzinfo classes may return absolutely anything.
        # Hence this paranoid conversion to create a valid cache key.
        tz_name = force_text(get_current_timezone_name(), errors='ignore')
        cache_key += '.%s' % tz_name.encode('ascii', 'ignore').decode('ascii').replace(' ', '_')
    return cache_key

def _generate_cache_header_key(key_prefix, request):
    """Returns a cache key for the header cache."""
    path = hashlib.md5(force_bytes(iri_to_uri(request.get_full_path())))
    cache_key = 'views.decorators.cache.cache_header.%s.%s' % (
        key_prefix, path.hexdigest())
    return _i18n_cache_key_suffix(request, cache_key)

def make_cache_key(request, key_prefix=None, method='GET'):
    """
    """
    if key_prefix is None:
        key_prefix = 'umkp_'
    return _generate_cache_header_key(key_prefix, request)
