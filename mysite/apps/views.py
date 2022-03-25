from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView

from django.contrib.auth import login,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

from PIL import Image

from .models import Items,Genres
from .forms import  ItemInfo, LoginForm, UserCreateForm
from .certification import certification

# ログインページ
class LoginView(LoginView):
    form_class = LoginForm
    template_name = "login.html"


# ログアウト機能
class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'login.html'


# ユーザー登録フロー1段階目、大学認証ページ
class UniversityRegisterView(TemplateView):
    def get(self, request):
        return render(request, 'university_register.html')

    def post(self, request,*args,**kwargs):
        # POSTにより画像データ、氏名を取得後certificetion.pyで認証
        img = Image.open(request.FILES["image"])
        first = request.POST["first"]
        last = request.POST["last"]
        if certification(img,first,last):
            # 認証成功時は次のページへ遷移
            return redirect("apps:signup")
        else:
            # 認証失敗時は再度登録画面が表示される
            return redirect("apps:university_register")


# ユーザー登録フロー2段階目、ユーザー情報入力ページ
class SignUpView(CreateView):
    form_class = UserCreateForm
    template_name = "user_register.html"
    # ユーザー登録成功時に遷移するページの指定
    success_url = reverse_lazy("apps:index")
    def form_valid(self,form):
        user = form.save()
        login(self.request,user,backend='django.contrib.auth.backends.ModelBackend')
        self.object = user
        return redirect(self.get_success_url())


# アプリケーションのトップページ
class IndexView(LoginRequiredMixin,TemplateView): 
    template_name = "index.html"
    login_url = '/'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        # modelから商品情報を取得
        context["item"] = Items.objects.all().values()
        # 取得した商品の画像情報のurlに余計ば部分があるので削除する
        for item in context["item"]:
            item["icon"] = item["icon"].replace("static/","")
        # modelからジャンル情報を取得
        context["genre"] = Genres.objects.all()
        return context

    # TODO 検索機能実装のためのPOST
    def post(self,request,*args,**kwargs):
        return 0


# 商品登録ページ
class ProductCreateView(LoginRequiredMixin,TemplateView):
    template_name = "product_create.html"
    login_url = '/'
    def get_context_data(self,**kwargs):
        # modelからジャンル情報を取得
        genres = Genres.objects.all()
        context = super().get_context_data(**kwargs)
        context["genre"] = genres
        return context

    def post(self, request,*args,**kwargs):
        form = ItemInfo(request.POST,request.FILES)
        # 登録成功後、indexページへと遷移
        if form.is_valid():
            form.save()
            return redirect("apps:index")



# ----------------------------------以下未実装のview-------------------------------------

# 購入・出品履歴の表示（未実装)
# class MyhistoryView(LoginRequiredMixin, TemplateView):
#     template_name = "myhistory.html"


# いいね機能実装後お気に入りリストの保管（未実装)
# class MylistView(TemplateView):
#     template_name = "mylist.html"


# 商品情報の編集ページ（未実装)
# class ProductRecreateView(LoginRequiredMixin, TemplateView):
#     login_url = '/'
#     def get_context_data(self,**kwargs):
#         genres = Genres.objects.all()
#         context = super().get_context_data(**kwargs)
#         context["genre"] = genres
#         return context
#     def post(self, request):
#         return 0


# 各商品ごとのページ(未実装)
# class ProductView(TemplateView):
#     login_url = '/'
#     def get(self, request):
#         return render(request, 'product.html')


# ユーザー情報の編集ページ(未実装)
# class UserEditView(LoginRequiredMixin, TemplateView):
#     login_url = '/'
#     def get(self, request):
#         return render(request, 'user_edit.html')
#     def post(self, request):
#         return 0

