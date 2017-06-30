from django.utils.translation import ugettext_lazy as _
from colab.plugins.utils.menu import colab_url_factory

name = 'colab_mkdocs'
verbose_name = 'Colab Mkdocs Plugin Plugin'

upstream = ''


urls = {
    'include': 'colab_mkdocs.urls',
    'prefix': '^mkdocs/',
}
