from django.db import models

# Create your models here.
class ChinaAdderss(models.Model):
    id = models.IntegerField(primary_key=True,default=None,auto_created=False,)
    name = models.CharField(max_length=255,null=True,default=None,verbose_name="行政区")
    pid = models.IntegerField(null=True,default=None,verbose_name="关联字段")

    class Meta:
        db_table = "china"
        verbose_name = '中国地址'
        verbose_name_plural = verbose_name

