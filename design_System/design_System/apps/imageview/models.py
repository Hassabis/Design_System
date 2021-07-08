from django.db import models

# Create your models here.
class Navimage(models.Model):

    imageurl = models.CharField(max_length=255)
    messageurl = models.CharField(max_length=255,default=None)

    class Meta:
        db_table = 'navimage'
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.imageurl