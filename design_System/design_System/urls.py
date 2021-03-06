"""design_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 用户中心
    url(r'^',include(('users.urls','users'),namespace="user")),
    # 资源图片管理
    url(r'^',include(('imageview.urls','imageview'),namespace="imageview")),
    # 汽车管理
    url(r'^',include(('car.urls','car'),namespace="car")),
    # 支付
    url(r'^',include(('payment.urls','payment'),namespace="payment")),
    # 地址
    url(r'^',include(('area.urls','area'),namespace="area"))
]
