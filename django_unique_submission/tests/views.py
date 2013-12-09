import json

from django.http import HttpResponse
from django_unique_submission import unique

@unique()
def echo(request):
    return HttpResponse(json.dumps({'method': request.method,
                                    'unique_token':request.session.unique_token }))
