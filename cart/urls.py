"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from cart import views

urlpatterns = [
    url(r'^add/$', views.cart_add, name='add'), # 添加购物车数据
    url(r'^count/$', views.cart_count, name='count'), # 获取用户购物车中商品的数量
    url(r'^$', views.cart_show, name='show'),
    url(r'^del/$', views.cart_del, name='delete'),
    url(r'^update/$', views.cart_update, name="update"),
]
