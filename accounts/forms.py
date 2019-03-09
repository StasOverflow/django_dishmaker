from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


class DishmakerUserCreationForm(UserCreationForm):

    CHOICES = [('Chef', _('Chef')),
               ('Customer', _('Customer'))]

    sign_up_as = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["sign_up_as"].label = _("Sign up as")

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data["sign_up_as"] == "Chef":
            user.is_staff = True
        if commit:
            user.save()
        return user
