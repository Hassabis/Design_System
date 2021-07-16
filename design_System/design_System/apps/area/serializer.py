# 最是人间留不住,朱颜辞镜花辞树
# -*- coding:utf-8 -*-
from rest_framework import serializers

from area.models import ChinaAdderss


class AdderssSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChinaAdderss
        fields = "__all__"