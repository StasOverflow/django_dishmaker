from django.shortcuts import render
from django.views.generic import TemplateView


class AizelParseView(TemplateView):
    template_name = "scrapy_aizel/index.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        # context['is_get'] = True
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
