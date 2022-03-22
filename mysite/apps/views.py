from re import template
from urllib import request
from django.shortcuts import render
from .models import Items
from .models import Genres

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView

from django.views import generic

# ログイン機能を必須にするには第一引数に(LoginRequiredMixin)を入れる
class IndexView(LoginRequiredMixin, generic.ListView): #ListViewに変更
    template_name = "index.html"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["item"] = Items.objects.all()
        context["genre"] = Genres.objects.all()
        return context

class LoginView(LoginView):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        return 0

class MailRegisterView(generic.TemplateView):
    def get(self, request):
        return render(request, 'mail_register.html')

    def post(self, request):
        return 0

class MyhistoryView(LoginRequiredMixin, generic.TemplateView):
    template_name = "myhistory.html"

class MylistView(LoginRequiredMixin, generic.ListView): #ListViewに変更
    template_name = "mylist.html"
        
class ProductCreateView(LoginRequiredMixin, generic.TemplateView):
    def get_context_data(self,**kwargs):
        items = Items.objects.all()
        genres = Genres.objects.all()
        context = super().get_context_data(**kwargs)
        context["item"] = items
        context["genre"] = genres
        return context
        
    def post(self, request):
        return 0

class ProductRecreateView(LoginRequiredMixin, generic.TemplateView):
    def get(self, request):
        return render(request, 'product_recreate.html')

    def post(self, request):
        return 0

class ProductView(LoginRequiredMixin, generic.TemplateView):
    def get(self, request):
        return render(request, 'product.html')

    def post(self, request):
        return 0

class UniversityRegisterView(generic.TemplateView):
    def get(self, request):
        return render(request, 'university_register.html')

    def post(self, request):
        return 0

class UserEditView(LoginRequiredMixin, generic.TemplateView):
    def get(self, request):
        return render(request, 'user_edit.html')

    def post(self, request):
        return 0

class UserRegisterView(generic.TemplateView):
    def get(self, request):
        return render(request, 'user_register.html')

    def post(self, request):
        return 0
