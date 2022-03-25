from re import I, template
from PIL import Image
from urllib import request
from django.shortcuts import render,redirect
from .models import Images, Items
from .models import Genres
from .forms import  CheckForm, EditItemForm,ItemInfo, LoginForm, UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView,CreateView

from django.views import generic
from .certification import certification
from django.contrib.auth.views import(LoginView, LogoutView)
from django.urls import reverse_lazy

# ログイン機能を必須にするには第一引数に(LoginRequiredMixin)を入れる
class IndexView(generic.TemplateView): #ListViewに変更
    template_name = "index.html"
    login_url = '/'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["item"] = Items.objects.all().values()
        for i in context["item"]:
            i["icon"] = i["icon"].replace("static/","")

        context["genre"] = Genres.objects.all()
        return context

    def post(self,request,*args,**kwargs):
        genre = request.POST["genre"]
        if genre != "":
            return redirect("apps:index")
        else:
            return redirect("apps:index")



class LoginView(LoginView):
    form_class = LoginForm
    template_name = "login.html"
    # def get(self, request):
    #     return render(request, 'login.html')

    # def post(self, request):
    #     form_class = LoginForm
    #     return 0

class MailRegisterView(generic.TemplateView):
    def get(self, request):
        return render(request, 'mail_register.html')

    def post(self, request):
        return 0

class MyhistoryView(LoginRequiredMixin, generic.TemplateView):
    template_name = "myhistory.html"

class MylistView(generic.TemplateView):
    template_name = "mylist.html"

class ProductCreateView(generic.TemplateView):
    template_name = "product_create.html"
    login_url = '/'
    def get_context_data(self,**kwargs):
        items = Items.objects.all()
        genres = Genres.objects.all()
        context = super().get_context_data(**kwargs)
        context["item"] = items
        context["genre"] = genres
        return context

    def post(self, request,*args,**kwargs):
        form = ItemInfo(request.POST,request.FILES)
        if form.is_valid():
            print("ok")
            form.save()
            return redirect("apps:index")



class ProductRecreateView(LoginRequiredMixin, generic.TemplateView):
    login_url = '/'
    def get_context_data(self,**kwargs):
        genres = Genres.objects.all()
        context = super().get_context_data(**kwargs)
        context["genre"] = genres
        return context

    def post(self, request):
        return 0

class ProductView(generic.TemplateView):
    login_url = '/'
    def get(self, request):
        return render(request, 'product.html')



class UniversityRegisterView(generic.TemplateView):
    def get(self, request):
        return render(request, 'university_register.html')

    def post(self, request,*args,**kwargs):
        img = Image.open(request.FILES["image"])
        first = request.POST["first"]
        last = request.POST["last"]
        if certification(img,first,last):
            return redirect("apps:signup")
        else:
            return redirect("apps:university_register")



class UserEditView(LoginRequiredMixin, generic.TemplateView):
    login_url = '/'
    def get(self, request):
        return render(request, 'user_edit.html')

    def post(self, request):
        return 0


class UserRegisterView(generic.TemplateView):
    def get(self, request):
        return render(request, 'user_register.html')

    def post(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('user_name')
            password = form.cleaned_data.get('user_pass')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/index")

class SignUpView(CreateView):
    form_class = UserCreateForm
    template_name = "user_register.html"
    success_url = reverse_lazy("apps:index")

    def form_valid(self,form):
        user = form.save()
        login(self.request,user,backend='django.contrib.auth.backends.ModelBackend')
        self.object = user
        return redirect(self.get_success_url())


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'accounts/login.html'