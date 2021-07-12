from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from car.models import CarType, CarLittleType, CarModel, CarDetailModel, CarDetailTechnicalData, TeMessage
from car.serializer import CarTypeSerializer, CarLittleTypeSerializer, CarModelSerializer, DetailCarModelSerialier, CarDetailTechnicalDataSerializer,TeMessageSerializer
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

class DetailCarModelView(APIView):
    def get(self,request,pk):
        try:
            # data = CarDetailModel.objects.filter(cartypesign=pk)
            data = CarDetailModel.objects.filter(cartypesign=pk)
        except:
            return Response({"errmsg":"我们也很困惑为什么查不出来"})
        ser = DetailCarModelSerialier(data,many=True)
        return Response(ser.data)

class TechinalCarData(APIView):
    def get(self,request,pk):
        """获取当前车俩的详情数据"""
        try:
            data = CarDetailTechnicalData.objects.get(technicalsign=pk)
        except:
            return Response({"error":"我们也很困惑为什么查不出来"})
        ser = CarDetailTechnicalDataSerializer(data)
        return Response(ser.data)


class TeCarBaseData(APIView):
    def get(self,request,pk):
        try:
            data = TeMessage.objects.get(tesign=pk)
        except:
            return Response({"error":"我们也很困惑为什么查不出来"})
        ser = TeMessageSerializer(data)
        return Response(ser.data)


