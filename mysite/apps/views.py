from re import template
from django.shortcuts import render


from django.views import generic

class IndexView(generic.TemplateView):
    template_name = "index.html"

class MyhistoryView(generic.TemplateView):
    template_name = "myhistory.html"

class MylistView(generic.TemplateView):
    template_name = "mylist.html"

class ProductCreateView(generic.TemplateView):
    template_name = "product_create.html"

class ProductRecreateView(generic.TemplateView):
    template_name = "product_recreate.html"

class ProductView(generic.TemplateView):
    template_name = "product.html"

class UserEditView(generic.TemplateView):
    template_name = "user_edit.html"
