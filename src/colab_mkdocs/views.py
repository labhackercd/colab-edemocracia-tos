from colab.plugins.views import ColabProxyView


class ColabMkdocsPluginProxyView(ColabProxyView):
    app_label = 'colab_mkdocs'
    diazo_theme_template = 'proxy/mkdocs.html'
