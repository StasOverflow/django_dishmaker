from accounts.forms import DishmakerUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.utils.translation import gettext_lazy as _


class SignUpView(generic.CreateView):
    form_class = DishmakerUserCreationForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'registration/sign_up_page.html'
    title = _('Sign Up')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = self.title
        return context
