import json
import re

from pymysql import DatabaseError
from django.views import View
from rest_framework.response import Response

from .models import User
from django.shortcuts import render, redirect
from .serializer import UserSerialzier
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
            user = User.objects.create_user(username=username, password=password, email=email)
        except DatabaseError:
            return http.JsonResponse({
                "err":"注册失败"
            })
        return http.JsonResponse({
            "msg":"success"
        })
