# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-15 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20180115_1813'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': '消息', 'verbose_name_plural': '消息'},
        ),
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(max_length=4000, verbose_name='消息'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='主题名称'),
        ),
    ]
