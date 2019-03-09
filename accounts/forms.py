from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from dishmaker.models import Dish, Ingredient, Order
from dishmaker.models import NotedItem
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission


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
            user.save()
            user.is_staff = True
            content_type = ContentType.objects.get_for_model(Dish)
            dish_permissions = Permission.objects.filter(content_type=content_type)
            content_type = ContentType.objects.get_for_model(Ingredient)
            ingredients_permissions = Permission.objects.filter(content_type=content_type)
            content_type = ContentType.objects.get_for_model(Order)
            order_permissions = Permission.objects.filter(content_type=content_type)
            content_type = ContentType.objects.get_for_model(NotedItem)
            noted_permissions = Permission.objects.filter(content_type=content_type)
            for perm in dish_permissions:
                user.user_permissions.add(perm)
            for perm in ingredients_permissions:
                user.user_permissions.add(perm)
            for perm in order_permissions:
                user.user_permissions.add(perm)
            for perm in noted_permissions:
                user.user_permissions.add(perm)
                print(perm.codename)
        if commit:
            user.save()
        return user
