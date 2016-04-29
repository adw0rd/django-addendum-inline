from django import VERSION as DJANGO_VERSION

from .views import InlineSaveView

if DJANGO_VERSION[:2] >= (1, 8):
    from django.conf.urls import url
    patterns = lambda *args: [a for a in args if a]
else:
    from django.conf.urls import patterns, url



urlpatterns = patterns(
    '',
    url(r'inline/save/$', InlineSaveView.as_view(), name='inline_save')
)
