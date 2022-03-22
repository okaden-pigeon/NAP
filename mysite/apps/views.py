from re import template
from urllib import request
from django.shortcuts import render
from .models import Items
from .models import Genres
from .forms import EditItemForm, LoginForm
from django.contrib.auth.models import User

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView

from django.views import generic

# ログイン機能を必須にするには第一引数に(LoginRequiredMixin)を入れる
class IndexView(generic.TemplateView): #ListViewに変更希望
    template_name = "index.html"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["item"] = Items.objects.all()
        context["genre"] = Genres.objects.all()
        return context

class LoginView(LoginView):
    def get(self, request):
        form_class = LoginForm
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

class MylistView(LoginRequiredMixin, generic.TemplateView): #ListViewに変更希望
    template_name = "mylist.html"
        
class ProductCreateView(LoginRequiredMixin, generic.TemplateView):
    def get_context_data(self, p, **kwargs):
        items = Items.objects.all()
        genres = Genres.objects.all()
        context = super().get_context_data(**kwargs)
        context["item"] = items
        context["genre"] = genres

        # URLからitem_idを取得
        request_item_id = p

        return context
        
    def post(self, request):
        return 0

class ProductRecreateView(LoginRequiredMixin, generic.TemplateView):

    def get_context_data(self, p, **kwargs):
        genres = Genres.objects.all()
        context = super().get_context_data(**kwargs)
        context["genre"] = genres

        # URLからitem_idを取得
        request_item_id = p

        return context

    def post(self, request):
        return 0

class ProductView(LoginRequiredMixin, generic.TemplateView):
    def get(self, p, request):

        # URLからitem_idを取得
        request_item_id = p

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

    def index(request): # product_recreate.html
        queryset = User.objects.get(id=request.user.id)

        initial_data = {
            'item_name': queryset.item_name,
        }

        form = EditItemForm(
            initial=initial_data
        )

        return render(request, 'apps/product_recreate.html', {"form": form})
