from django.conf.urls import patterns, url

from .views import InlineSaveView


urlpatterns = patterns(
    '',
    url(r'inline/save/$', InlineSaveView.as_view(), name='inline_save')
)
