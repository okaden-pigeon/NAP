from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static 

from . import views
import mysite.settings

import sys
sys.path.append("../")


app_name = 'apps'
urlpatterns = [
    # ログインページ
    path('', views.LoginView.as_view(), name="login"),
    # ログアウト
    path('logout/', views.Logout.as_view(), name='logout'),
    # 大学認証ページ
    path('university_register/', views.UniversityRegisterView.as_view(), name="university_register"),
    # ユーザー登録ページ
    path("user_register/",views.SignUpView.as_view(),name="signup"),
    # 商品一覧ページ
    path('index', views.IndexView.as_view(), name="index"),
    # 商品登録ページ
    path('product_create/', views.ProductCreateView.as_view(), name="product_create"),

# ------------------------以下未実装のルーティング------------------------------
    # path('myhistory/', views.MyhistoryView.as_view(), name="myhistory"),
    # path('mylist/', views.MylistView.as_view(), name="mylist"),
    # path('product_recreate/', views.ProductRecreateView.as_view(), name="product_recreate"),
    # path('product/', views.ProductView.as_view(), name="product"),
    # path('user_edit/', views.UserEditView.as_view(), name="user_edit"),
# ------------------------未実装のルーティングここまで--------------------------
    ]

# 画像をstaticから利用するための設定
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(mysite.settings.MEDIA_URL,document_root=mysite.settings.MEDIA_ROOT)
