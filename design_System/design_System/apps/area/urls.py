# 最是人间留不住,朱颜辞镜花辞树
# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views
urlpatterns = [
    url("province/",views.getProvince.as_view()),
    url("city/(?P<pk>\d+)/",views.getCity.as_view()),
    url("district/(?P<pk>\d+)/",views.getDistrict.as_view()),
]