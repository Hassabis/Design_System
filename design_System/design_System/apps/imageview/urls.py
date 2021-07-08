# 最是人间留不住,朱颜辞镜花辞树
# -*- coding:utf-8 -*-
from django.conf.urls import url
from django.urls import include, path
from . import views
urlpatterns = [
    path('indeximage/',views.NavView.as_view())
    # path('register/',views.UserRegister.as_view())
]