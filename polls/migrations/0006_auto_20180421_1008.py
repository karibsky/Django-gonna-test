# Generated by Django 2.0.4 on 2018-04-21 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20180421_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=500, verbose_name='Описание'),
        ),
    ]
