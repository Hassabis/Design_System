from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from area.models import ChinaAdderss
from area.serializer import AdderssSerializer


class getProvince(APIView):
    def get(self,request):
        try:
            datas = ChinaAdderss.objects.filter(pid=0)
        except:
            return Response({"error":"服务器错误"})
        ser = AdderssSerializer(datas,many=True)
        return Response(ser.data)

class getCity(APIView):
    def get(self,request,pk):
        try:
            datas = ChinaAdderss.objects.filter(pid=pk)
        except:
            return Response({"error":"服务器错误"})
        ser = AdderssSerializer(datas,many=True)
        return Response(ser.data)
class getDistrict(APIView):
    def get(self,request,pk):
        try:
            print(pk)
            datas = ChinaAdderss.objects.filter(pid=pk)
        except Exception as e:
            print(e)
            return Response({"error":"服务器错误"})
        ser = AdderssSerializer(datas,many=True)
        return Response(ser.data)


