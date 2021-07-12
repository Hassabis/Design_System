# 最是人间留不住,朱颜辞镜花辞树
# -*- coding:utf-8 -*-
from rest_framework import serializers
from .models import User, AdderssManger


class UserSerialzier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class AdderssSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdderssManger
        fields = "__all__"
