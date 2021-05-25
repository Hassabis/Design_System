from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    mobile = models.CharField(max_length=11,unique=False,verbose_name="手机号")
    birthday = models.CharField(verbose_name="生日",max_length=16)
    profession = models.CharField(max_length=9,verbose_name="职业")


    class Meta:
        db_table = 'useraccount'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

