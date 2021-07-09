from django.db import models

# Create your models here.

class CarModel(models.Model):
    cartype = models.CharField(max_length=255,unique=True,default=None,verbose_name="汽车型号"),
    carbacimage = models.CharField(max_length=255,default=None,verbose_name="汽车展示背景图")
    carmodel = models.CharField(max_length=255,default=None,verbose_name="汽车模型")
    carprice = models.CharField(max_length=99,default=None,verbose_name="汽车价格")
    carpower = models.CharField(max_length=255,default=None,verbose_name="汽车功率")
    carspeeds = models.IntegerField(default=None,verbose_name="百公里加速耗时")
    cartime = models.IntegerField(default=None,verbose_name="百公里")
    carsign = models.IntegerField(default=None,verbose_name="标识")

    class Meta:
        db_table = "tb_carmessage"
        verbose_name = '汽车信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.cartype



class CarType(models.Model):
    carheader = models.CharField(max_length=255,default=None,verbose_name="汽车分类")
    carsign = models.IntegerField(default=None)

    class Meta:
        db_table = "tb_classification"
        verbose_name = '汽车信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.carheader

class CarLittleType(models.Model):
    little = models.CharField(max_length=99,verbose_name="车型")
    sign = models.IntegerField(verbose_name="标识",default=None)

    class Meta:
        db_table = "tb_littertype"
        verbose_name = '汽车型号'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.little

