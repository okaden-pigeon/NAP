from django import forms

from .models import Check, Items, Users

class EditItemForm(forms.Form):
    item_name = forms.CharField(max_length=40)

# class CheckForm(forms.ModelForm):
#     class Meta:
#         model = Check
#         fields = ["image"]

class ItemInfo(forms.ModelForm):
    class Meta:
        model = Items
        fields = ["item_name","item_description","icon"]