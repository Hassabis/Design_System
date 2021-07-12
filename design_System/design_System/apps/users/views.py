import json
import re

from pymysql import DatabaseError
from django.views import View
from rest_framework.response import Response

from .models import User, AdderssManger
from django.shortcuts import render, redirect
from .serializer import UserSerialzier,AdderssSerializer
from rest_framework.views import APIView
from django import http
# Create your views here.
class UserRegister(View):
    def post(self,request):
        data = request.body.decode()
        data_dict = json.loads(data)
        username = data_dict.get("username")
        password = data_dict.get("password")
        password2 = data_dict.get("password2")
        email = data_dict.get("email")
        #后端效验
        if not all([username,password,password2,email]):
            return http.HttpResponseForbidden('缺少参数')

        if not re.match(r'^[0-9A-Za-z]{8,12}$', password):
            return http.HttpResponseForbidden('请输入8-12位的密码')
        try:
            User.objects.create_user(username=username, password=password, email=email)
        except DatabaseError:
            return http.JsonResponse({
                "err":"注册失败"
            })
        return http.JsonResponse({
            "msg":"success"
        })

    def get(self,requests):
        username = requests.GET.get("username")
        print(username)
        count = User.objects.filter(username=username).count()
        return http.JsonResponse({"code": 0, "errmsg": '该用户已经存在', 'count': count})
class UserProcess(APIView):
    def put(self,request):
        """修改用户个人信息"""
        result = request.data.get("data")
        uid = request.data.get("uid")
        date = str(result.get("date1")).split("T")[0]
        print(result.get("region"))
        # print(User.objects.get(id = uid).username)
        # if result.get("name") == User.objects.get(id = uid).username:
        #     return Response({"error":"用户名已经存在"})
        try:
            User.objects.filter(id = uid).update(
                username = result.get("name"),
                profession = result.get("Mprofession"),
                birthday = date,
                gender = False if result.get("region") == "female" else True
            )
            user = User.objects.get(id=uid)
        except Exception as e:
            print(e)
            return Response({"error":"我佛了，又特么报错？"})
        ser = UserSerialzier(user)
        return Response(ser.data)


class GetAdderss(APIView):
    def get(self,request,pk):
        try:
            adderss = AdderssManger.objects.filter(adderssid=pk)
        except Exception as e:
            print(e)
            return Response({"error":"获取地址出错，请重试"})
        ser = AdderssSerializer(adderss,many=True)
        return Response(ser.data)



