from django.urls import path

from . import views

app_name = 'apps'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('myhistory/', views.MyhistoryView.as_view(), name="myhistory"),
    path('mylist/', views.MylistView.as_view(), name="mylist"),
    path('product_create/', views.ProductCreateView.as_view(), name="product_create"),
    path('product_recreate/', views.ProductRecreateView.as_view(), name="product_recreate"),
    path('product/', views.ProductView.as_view(), name="product"),
    path('user_edit/', views.UserEditView.as_view(), name="user_edit"),
    path('user_register/', views.UserRegisterView.as_view(), name="user_register"),

]