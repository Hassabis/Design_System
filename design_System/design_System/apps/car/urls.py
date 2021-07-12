# 最是人间留不住,朱颜辞镜花辞树
# -*- coding:utf-8 -*-
from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    # 车的一级分类
    path('Firstclasscar/',views.NavCarMessage.as_view()),
    # 车的二级分类
    url('Secondclasscar/(?P<pk>\d+)/',views.LittleCarType.as_view()),
    # 汽车详情
    url('Thirdclasscar/(?P<pk>\d+)/',views.DetailCarMessage.as_view()),
    # 某一个分类的所有汽车
    url('detailCar/(?P<pk>\d+)/',views.DetailCarModelView.as_view()),
    # 车辆详情数据
    url('techincalCar/(?P<pk>\d+)/',views.TechinalCarData.as_view()),
    # 页面基本数据
    url('pagemessage/(?P<pk>\d+)/',views.TeCarBaseData.as_view())
]