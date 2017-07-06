# -*- coding: utf-8 -*-

name = 'colab_mkdocs'
verbose_name = 'Colab Mkdocs Plugin Plugin'

upstream = ''

docs_title = "Sobre"

pages = {
    'Home': 'index.md',
    'Termos de Serviço': 'tos.md'
}


urls = {
    'include': 'colab_mkdocs.urls',
    'prefix': '^mkdocs/',
}
