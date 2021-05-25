# 最是人间留不住,朱颜辞镜花辞树
# -*- coding:utf-8 -*-
from django.conf.urls import url
from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token
from . import views
urlpatterns = [
    url(r'^login/$',obtain_jwt_token),
    path('register/',views.UserRegister.as_view())
]