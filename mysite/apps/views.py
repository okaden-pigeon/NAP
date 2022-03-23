from re import template
from urllib import request
from django.shortcuts import render,redirect
from .models import Items
from .models import Genres
from .forms import  EditItemForm,ItemInfo
from django.contrib.auth.models import User

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView

from django.views import generic
from .jobs.certification import certification

# ログイン機能を必須にするには第一引数に(LoginRequiredMixin)を入れる
class IndexView(generic.TemplateView): #ListViewに変更
    template_name = "index.html"
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

class MylistView(generic.TemplateView): #ListViewに変更
    template_name = "mylist.html"
        
class ProductCreateView(generic.TemplateView):
    template_name = "product_create.html"
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

    def get_context_data(self,**kwargs):
        genres = Genres.objects.all()
        context = super().get_context_data(**kwargs)
        context["genre"] = genres
        return context

    def post(self, request):
        return 0

def product(request):
    if request.method == "POST":
        return render(request,"product.html")
    else:
        return render(request,"product.html") 

class ProductView(LoginRequiredMixin, generic.TemplateView):
    def get(self, request):
        return render(request, 'product.html')

    def post(self, request):
        return 0

class UniversityRegisterView(generic.TemplateView):
    def get(self, request):
        return render(request, 'university_register.html')

    # def post(self, request,*args,**kwargs):
    #     # first = self.request.POST
    #     form = CheckForm(request.POST,request.FILES)
    #     if form.is_valid():
    #         print("ok")
    #         form.save()
    #     file = Check.objects.get(pk=1)
    #     if ():
    #         return redirect("user_register.html")
    #     else:
    #         return render(request,"university_register.html",context = {"alert":"error"})
        
# def university_register(request):
#     first = request.POST.get("first",None)
#     last = request.POST.get("last",None)
#     file = request.POST.get("photo",None)
#     university = request.POST.get("university",None)
#     form = ItemInfo(request.POST,request.FILES)
#     if (True):
#         return render(request,"user_register/",{"university:university})
#     else:
#         return render(request,"university_register.html",context = {"alert":"error"}) 


class UserEditView(LoginRequiredMixin, generic.TemplateView):
    def get(self, request):
        return render(request, 'user_edit.html')

    def post(self, request):
        return 0

def user_register(request):
    if request.method == "POST":
    #     form = UserInfo(request.POST,request.FILES)
    #     if form.is_valid():
    #         form.save()
            return redirect("/")
    else:
        return render(request,"user_register.html")

# class UserRegisterView(generic.TemplateView):
#     def get(self, request):
#         return render(request, 'user_register.html')

#     def post(self, request):
#         return 0

    # def index(request): # product_recreate.html
    #     queryset = User.objects.get(id=request.user.id)

    #     initial_data = {
    #         'item_name': queryset.item_name,
    #     }

    #     form = EditItemForm(
    #         initial=initial_data
    #     )

    #     return render(request, 'apps/product_recreate.html', {"form": form})
