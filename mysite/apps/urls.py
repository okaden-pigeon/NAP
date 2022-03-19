from django.urls import path

from . import views

app_name = 'apps'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('mail_register/', views.MailRegisterView.as_view(), name="mail_register"),
    path('myhistory/', views.MyhistoryView.as_view(), name="myhistory"),
    path('mylist/', views.MylistView.as_view(), name="mylist"),
    path('product_create/', views.ProductCreateView.as_view(), name="product_create"),
    path('product_recreate/', views.ProductRecreateView.as_view(), name="product_recreate"),
    path('product/', views.ProductView.as_view(), name="product"),
    path('university_register/', views.UniversityRegisterView.as_view(), name="university_register"),
    path('user_edit/', views.UserEditView.as_view(), name="user_edit"),
    path('user_register/', views.UserRegisterView.as_view(), name="user_register"),
    # メールアドレス認証 https://blog.narito.ninja/detail/42/#_4
    path('user_create/', views.UserCreate.as_view(), name='user_create'),
    path('user_create/done', views.UserCreateDone.as_view(), name='user_create_done'),
    path('user_create/complete/<token>/', views.UserCreateComplete.as_view(), name='user_create_complete'),
]