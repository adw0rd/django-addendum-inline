from django.conf.urls import patterns, url

from .views import InlineSaveView


urlpatterns = patterns(
    '',
    url(r'inline/(?P<key>[^/]+)/$', InlineSaveView.as_view(), name='inline_save')
)
