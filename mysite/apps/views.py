from re import template
from django.shortcuts import render
from .models import Items
from .models import Genres
from .forms import EditItemForm
from django.contrib.auth.models import User

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired, loads, dumps
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.views import generic
from .forms import (
    LoginForm, UserCreateForm
)

# ログイン機能を必須にするには第一引数に(LoginRequiredMixin)を入れる
class IndexView(generic.TemplateView):
    template_name = "index.html"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["item"] = Items.objects.all()
        context["genre"] = Genres.objects.all()
        return context

class LoginView(LoginView):
    template_name = "login.html"

class MailRegisterView(generic.TemplateView):
    template_name = "mail_register.html"

class MyhistoryView(generic.TemplateView):
    template_name = "myhistory.html"

class MylistView(generic.TemplateView):
    template_name = "mylist.html"
    def get_context_data(self,**kwargs):
        items = Items.objects.all()
        context = super().get_context_data(**kwargs)
        context["item"] = items
        return context

class ProductCreateView(generic.TemplateView):
    template_name = "product_create.html"
    def get_context_data(self,**kwargs):
        genres = Genres.objects.all()
        context = super().get_context_data(**kwargs)
        context["genre"] = genres
        return context

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

def index(request): # product_recreate.html
    queryset = User.objects.get(id=request.user.id)

    initial_data = {
        'item_name': queryset.item_name,
    }

    form = EditItemForm(
        initial=initial_data
    )

    return render(request, 'apps/product_recreate.html', {"form": form})