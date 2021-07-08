# 最是人间留不住,朱颜辞镜花辞树
# -*- coding:utf-8 -*-
from rest_framework import serializers

from imageview.models import Navimage


class NavimageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Navimage
        fields = ("imageurl",)