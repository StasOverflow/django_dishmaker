from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout, login


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'registration/sign_up_page.html'
    title = 'Sign Up'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = self.title
        return context

#
# class LogoutView(generic.RedirectView):
#     """
#     Provides users the ability to logout
#     """
#     url = reverse_lazy('dishmaker:index')
#
#     def get(self, request, *args, **kwargs):
#         logout(request)
#         return super(LogoutView, self).get(request, *args, **kwargs)
#
#
# class LoginView(generic.FormView):
#     success_url = '/home/'
#     form_class = AuthenticationForm
#
#     # @method_decorator(sensitive_post_parameters('password'))
#     # @method_decorator(csrf_protect)
#     # @method_decorator(never_cache)
#     def dispatch(self, request, *args, **kwargs):
#         # Sets a test cookie to make sure the user has cookies enabled
#         request.session.set_test_cookie()
#
#         return super(LoginView, self).dispatch(request, *args, **kwargs)
#
#     def form_valid(self, form):
#         login(self.request, form.get_user())
#
#         # If the test cookie worked, go ahead and
#         # delete it since its no longer needed
#         if self.request.session.test_cookie_worked():
#             self.request.session.delete_test_cookie()
#
#         return super(LoginView, self).form_valid(form)
#
#     def get_success_url(self):
#         redirect_to = self.request.REQUEST.get(self.redirect_field_name)
#         if not is_safe_url(url=redirect_to, host=self.request.get_host()):
#             redirect_to = self.success_url
#         return redirect_to
