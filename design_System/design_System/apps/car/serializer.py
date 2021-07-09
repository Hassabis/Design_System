# 最是人间留不住,朱颜辞镜花辞树
# -*- coding:utf-8 -*-
from rest_framework import serializers

from car.models import CarModel, CarType, CarLittleType


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        # 车的详情
        model = CarModel
        fields = "__all__"


class CarTypeSerializer(serializers.ModelSerializer):
    class Meta:
        # 车的大分类
        model = CarType
        fields = "__all__"


class CarLittleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        # 二级分类
        model = CarLittleType
        fields = "__all__"
