from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from car.models import CarType, CarLittleType, CarModel
from car.serializer import CarTypeSerializer, CarLittleTypeSerializer, CarModelSerializer
from rest_framework.response import Response


class NavCarMessage(APIView):
    def get(self, request):
        """获取所有一级分类"""
        try:
            cartype = CarType.objects.all()
        except:
            return Response({"errormsg": "我们也很困惑为什么查不出来"})
        ser = CarTypeSerializer(cartype, many=True)
        return Response(ser.data)


class LittleCarType(APIView):
    def get(self, request, pk):
        """根据传入的id值获取二级分类"""
        try:
            littletype = CarLittleType.objects.filter(sign=pk)
        except:
            return Response({"errmsg": "我们也很困惑为什么查不出来"})
        ser = CarLittleTypeSerializer(littletype, many=True)
        return Response(ser.data)

class DetailCarMessage(APIView):
    def get(self,request,pk):
        """根据二级分类的id返回汽车详情数据"""
        try:
            carmessage = CarModel.objects.filter(carsign = pk)
        except Exception as e:
            # print(e)
            return Response({"errormsg":"我们也很困惑为什么查不出来"})
        ser = CarModelSerializer(carmessage,many=True)
        return Response(ser.data)

