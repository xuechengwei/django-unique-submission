from django.conf.urls import patterns, url


urlpatterns = patterns('django_unique_submission.tests.views',
                        url(r'^echo/$', 'echo', name='echo'),)
