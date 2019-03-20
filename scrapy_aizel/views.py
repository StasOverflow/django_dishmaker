from django.shortcuts import render
from django.views.generic import TemplateView
import redis
import dish_composer.settings as s


class AizelParseView(TemplateView):

    redis_connection = redis.Redis(host=s.REDIS_HOST, port=s.REDIS_PORT)
    title = 'Hi, wanna activate a parser?'
    template_name = "scrapy_aizel/index.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['title'] = self.title
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.redis_connection.lpush('aizel:start_urls', "https://aizel.ru/ua-ru/odezhda/bryuki/")
        return super().get(request, *args, **kwargs)
