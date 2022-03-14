from django.urls import path

from . import views

app_name = 'apps'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('myhistory/', views.MyhistoryView.as_view(), name="myhistory"),
    path('mylist/', views.MylistView.as_view(), name="mylist"),
    path('product-create/', views.ProductCreateView.as_view(), name="product_create"),
    path('product-recreate/', views.ProductRecreateView.as_view(), name="product_recreate"),
    path('product/', views.ProductView.as_view(), name="product"),
    path('useredit/', views.UserEditView.as_view(), name="user_edit"),

    path('accounts/', include('accounts.urls')), # django学習帳 3-1
]