from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView
import redis
import dish_composer.settings as s
from scrapy_aizel.models import AizelClothItem


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
        return redirect(reverse('dishmaker:order_from_dish',
                                kwargs={'dish_id': request.POST.get('dish_id')}),
                        )


class AizelListView(ListView):
    template_name = "scrapy_aizel/clothes_list.html"
    title = 'Clothes '
    context_object_name = 'clothes'  # Default: object_list
    paginate_by = 10
    queryset = AizelClothItem.objects.all()  # Default: Model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context
