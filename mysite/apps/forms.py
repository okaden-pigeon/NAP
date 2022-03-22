from django import forms

class EditItemForm(forms.Form):
    item_name = forms.CharField(max_length=40)