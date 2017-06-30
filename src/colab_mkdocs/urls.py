
from django.conf.urls import patterns, url
from django.views.decorators.clickjacking import xframe_options_exempt

from .views import ColabMkdocsPluginProxyView


urlpatterns = patterns(
    '',
    url(r'^(?P<path>.*)$',
        xframe_options_exempt(ColabMkdocsPluginProxyView.as_view()),
        name='colab_mkdocs'),
)
