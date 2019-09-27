# -*- coding:utf-8 -*-

'''定义learning_logs的url模式'''
from django.conf.urls import url
from . import views
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register'),

]
