import json

from django.views.generic import View
from django.core.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Snippet
from .utils import has_permission


class InlineSaveView(View):
    http_method_names = ['post']

    @csrf_exempt
    def dispatch(self, request, key):
        if not has_permission(request.user):
            raise PermissionDenied
        text = request.POST.get('value')
        snippet, cr = Snippet.objects.get_or_create(
            key=key, defaults=dict(
                text=text
            )
        )
        if not cr:
            Snippet.objects.filter(pk=snippet.pk).update(text=text)
        return HttpResponse(
            json.dumps({'state': True}),
            content_type="application/json"
        )
