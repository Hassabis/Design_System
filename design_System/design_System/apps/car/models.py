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
    detailsign = models.IntegerField(default=None)

    class Meta:
        db_table = "tb_littertype"
        verbose_name = '汽车型号'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.little

class CarDetailModel(models.Model):
    carmodel = models.CharField(max_length=255,default=None,verbose_name="汽车模型",null=True)
    carprice = models.CharField(max_length=99,default=None,verbose_name="汽车价格",null=True)
    carpower = models.CharField(max_length=255,default=None,verbose_name="汽车功率",null=True)
    carspeeds = models.FloatField(default=None,verbose_name="百公里加速耗时",null=True)
    cartime = models.FloatField(default=None,verbose_name="百公里",null=True)
    cartypesign = models.FloatField(default=None,verbose_name="标识",null=True)
    carheader = models.CharField(max_length=255,null=True,default=None)

    class Meta:
        db_table = "tb_detailcarmodel"
        verbose_name = '汽车型号'
        verbose_name_plural = verbose_name
class CarDetailTechnicalData(models.Model):
    name = models.CharField(max_length=255,default=None,null=True)
    technicalsign = models.IntegerField(verbose_name="标识",null=True)
    number_of_cylinders = models.IntegerField(verbose_name="气缸数",null=True)
    displacement = models.CharField(max_length=255,verbose_name="排量",null=True)
    bestpower = models.FloatField(verbose_name="最大功率",null=True)
    maxtorque = models.IntegerField(verbose_name="最大扭矩",null=True)
    mostpowerspeed = models.IntegerField(verbose_name="最大功率对应最大转速",null=True,default=None)
    maximumSpeed = models.IntegerField(verbose_name="最大扭矩对应发动机转速范围",null=True)
    maxspeed = models.FloatField(verbose_name="最高时速",null=True)
    enginemostspeed = models.IntegerField(default=None,null=True,verbose_name="发动机最高转速")
    zerohundertime = models.FloatField(verbose_name="0-100加速时间",null=True)
    zerohuntersix = models.FloatField(verbose_name="0-160加速时间",null=True)
    eightspped = models.FloatField(verbose_name="80-120km/h超车加速时间",null=True)
    carlong = models.FloatField(verbose_name="长度",null=True)
    carwidth = models.FloatField(null=True,verbose_name="宽度")
    carwidthmirror = models.FloatField(null=True,verbose_name="宽度(带后视镜)")
    carheight = models.FloatField(null=True,verbose_name="高度")
    wheelbase = models.IntegerField(null=True,verbose_name="轴距")
    weight = models.IntegerField(null=True,verbose_name="重量")
    contentarea = models.IntegerField(null=True,verbose_name="行李厢容积(前)")
    mostcontentarea = models.IntegerField(null=True,verbose_name="最大行李厢容积")
    oilbox = models.IntegerField(null=True,verbose_name="燃油箱")
    price = models.CharField(null=True,verbose_name="价格",max_length=144)
    carimage = models.CharField(null=True,default=None,max_length=255,verbose_name="汽车图片")

    class Meta:
        db_table = "tb_alldata"
        verbose_name = '汽车详情数据'
        verbose_name_plural = verbose_name

class TeMessage(models.Model):
    tesign = models.IntegerField(verbose_name="标志",null=True)
    firsttitle = models.CharField(max_length=255,verbose_name="标题一")
    firsttext = models.CharField(max_length=255,verbose_name="文本一")
    videoone = models.CharField(max_length=255,verbose_name="视频一")
    secondtitle = models.CharField(max_length=100,verbose_name="标题二")
    secondtext = models.CharField(max_length=255,verbose_name="文本二")
    videotwo = models.CharField(max_length=255,verbose_name="视频二")
    thirddtitle = models.CharField(max_length=100,verbose_name="标题三")
    thirdtext = models.CharField(max_length=255,verbose_name="文本三")
    videothree = models.CharField(max_length=255,verbose_name="视频三")
    fourdtitle = models.CharField(max_length=100,verbose_name="标题四")
    fourtext = models.CharField(max_length=255,verbose_name="文本四")
    videofour = models.CharField(max_length=255,verbose_name="视频四")
    class Meta:
        db_table = "tb_te"
        verbose_name = '详情页基本信息'
        verbose_name_plural = verbose_name



