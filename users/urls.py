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
from django.conf.urls import url
from django.contrib import admin
from users import views

urlpatterns = [
    url(r'^register/$', views.register,name='register'),
    url(r'^register_handle/$',views.register_handle,name='register_handle'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login_check/$', views.login_check, name='login_check'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^address/$', views.address, name='address'),
    url(r'^order/(?P<page>\d+)?/?$', views.order, name='order'), # 用户中心-订单页  增加分页功能
    url(r'^active/(?P<token>.*)/$', views.register_active, name='active'),  # 用户激活
    url(r'^verifycode/$', views.verifycode, name='verifycode'), # 验证码功能
    url(r'^$', views.user, name='user'),
]
