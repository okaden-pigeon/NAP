from re import template
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from  .forms import LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic

# ログイン機能を必須にするには第一引数に(LoginRequiredMixin)を入れる
class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = "index.html"

class LoginView(LoginView):
    template_name = "login.html"
    form_class = LoginForm

class MailRegisterView(generic.TemplateView):
    template_name = "mail_register.html"

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

class UniversityRegisterView(generic.TemplateView):
    template_name = "university_register.html"

class UserEditView(generic.TemplateView):
    template_name = "user_edit.html"

class UserRegisterView(generic.TemplateView):
    template_name = "user_register.html"
