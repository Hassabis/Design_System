from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from imageview.models import Navimage
from rest_framework.response import Response

from imageview.serializer import NavimageSerializer


class NavView(APIView):
    def get(self,req):
        """获取首页轮播图"""
        try:
            images = Navimage.objects.all()
        except:
            return Response({"errmsg":"服务器错误","stateCode":"500"})
        ser = NavimageSerializer(images,many=True)
        return Response(ser.data)
