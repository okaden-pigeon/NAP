from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label #全てのフォームの部品にplaceholderを定義して、入力フォームにフォーム名が表示されるように指定する


from .models import Users

class EditItemForm(forms.Form):
    item_name = forms.CharField(max_length=40)

class UserInfo(forms.ModelForm):
    class Meta:
        model = Users
        fields = ("user_name","user_pass","icon")