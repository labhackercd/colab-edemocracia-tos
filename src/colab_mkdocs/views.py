from colab.plugins.views import ColabProxyView
from django.contrib.staticfiles.views import serve
from django.http import HttpResponse
from revproxy.transformer import DiazoTransformer
import os


class ColabMkdocsPluginProxyView(ColabProxyView):
    app_label = 'colab_mkdocs'
    diazo_theme_template = 'proxy/mkdocs.html'

    def dispatch(self, request, path):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        docs_path = os.path.join(dir_path, path)

        if os.path.isdir(docs_path):
            path = os.path.join(path, 'index.html')

        path = os.path.join('mkdocs_build', path)

        file_response = serve(request, path, insecure=True)
        response = HttpResponse(file_response.streaming_content,
                                content_type=file_response.get('Content-type'))
        diazo = DiazoTransformer(request, response)

        response = diazo.transform(self.diazo_rules, self.diazo_theme_template,
                                   self.html5)
        return response
