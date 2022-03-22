from django import forms

class EditItemForm(forms.Form):
    item_name = forms.CharField()