# 最是人间留不住,朱颜辞镜花辞树
# -*- coding:utf-8 -*-
from rest_framework import serializers

from car.models import CarModel, CarType, CarLittleType, CarDetailModel, CarDetailTechnicalData, TeMessage


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


class DetailCarModelSerialier(serializers.ModelSerializer):
    class Meta:
        model = CarDetailModel
        fields = "__all__"


class CarDetailTechnicalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDetailTechnicalData
        fields = "__all__"


class TeMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeMessage
        fields = "__all__"
