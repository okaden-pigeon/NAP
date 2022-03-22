"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# django学習帳 1-3
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), #マイグレーション前にコメントアウト
    path('', include('apps.urls')),
    # 以下コメントアウトはずした（たいち）
    path('accounts/', include('allauth.urls')),
    # path('accounts/', include('accounts.urls')), # django学習帳 3-1
    # path('', include('register.urls')), # https://blog.narito.ninja/detail/40/
]
