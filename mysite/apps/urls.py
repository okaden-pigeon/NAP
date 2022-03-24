from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static 
import sys
sys.path.append("../")

from . import views
import mysite.settings

app_name = 'apps'
urlpatterns = [
    path('index', views.IndexView.as_view(), name="index"),
    path('', views.LoginView.as_view(), name="login"),
    path('mail_register/', views.MailRegisterView.as_view(), name="mail_register"),
    path('myhistory/', views.MyhistoryView.as_view(), name="myhistory"),
    path('mylist/', views.MylistView.as_view(), name="mylist"),
    path('product_create/', views.ProductCreateView.as_view(), name="product_create"),
    path('product_recreate/', views.ProductRecreateView.as_view(), name="product_recreate"),
    path('product/', views.ProductView.as_view(), name="product"),
    path('university_register/', views.UniversityRegisterView.as_view(), name="university_register"),
    path('user_edit/', views.UserEditView.as_view(), name="user_edit"),
    path('user_register/', views.UserRegisterView.as_view(), name="user_register"),
    ]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(mysite.settings.MEDIA_URL,document_root=mysite.settings.MEDIA_ROOT)
