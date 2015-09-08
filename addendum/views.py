import json

from django.views.generic import View
from django.core.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404
from .models import Snippet
from .utils import has_permission


class InlineSaveView(View):
    http_method_names = ['post']

    @csrf_exempt
    def dispatch(self, request):
        if not has_permission(request.user):
            raise PermissionDenied
        key = request.GET.get('key', None)
        if not key:
            raise Http404
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
