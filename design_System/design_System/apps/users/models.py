from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    mobile = models.CharField(max_length=11,unique=False,verbose_name="手机号")
    birthday = models.CharField(verbose_name="生日",max_length=16)
    profession = models.CharField(max_length=9,verbose_name="职业")
    gender = models.BooleanField(verbose_name="性别",default=False)
    class Meta:
        db_table = 'useraccount'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

class AdderssManger(models.Model):
    adderssid = models.IntegerField(verbose_name="地址归属用户")
    adderssusername = models.CharField(max_length=255,verbose_name="用户姓名",default=None)
    if_default = models.BooleanField(default=False)
    phone = models.CharField(max_length=255,default=None)
    adderss = models.CharField(max_length=255,default=None)

    class Meta:
        db_table = 'tb_adderss'
        verbose_name = '地址管理'
        verbose_name_plural = verbose_name