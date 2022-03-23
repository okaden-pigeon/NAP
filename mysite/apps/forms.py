from django import forms

from .models import Items, Users

class EditItemForm(forms.Form):
    item_name = forms.CharField(max_length=40)

class UserInfo(forms.ModelForm):
    class Meta:
        model = Users
        fields = ("user_name","user_pass","icon")

class ItemInfo(forms.ModelForm):
    class Meta:
        model = Items
        fields = ["item_name","item_description","icon"]