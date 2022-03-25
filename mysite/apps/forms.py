from django import forms

from .models import  Images, Items

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm 


class EditItemForm(forms.Form):
    item_name = forms.CharField(max_length=40)

class CheckForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ["image","first","last"]

class ItemInfo(forms.ModelForm):
    class Meta:
        model = Items
        fields = ["item_name","item_description","icon"]

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = fields = ["username", "email", "password1"]


class LoginForm(AuthenticationForm):
    """ログオンフォーム"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label   