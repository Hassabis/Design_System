# Generated by Django 3.1.7 on 2021-07-09 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0005_remove_cartype_carinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartype',
            name='carsign',
            field=models.IntegerField(default=None),
        ),
    ]
