# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-10 19:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20180303_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(default='n/a', max_length=128, verbose_name='日志标识')),
                ('closed', models.BooleanField(default=False, verbose_name='是否关闭')),
                ('cmd_count', models.IntegerField(default=0, verbose_name='命令执行数量')),
                ('stay_time', models.IntegerField(default=0, help_text='每次刷新自动计算停留时间', verbose_name='停留时长(seconds)')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='查询时间')),
            ],
            options={
                'verbose_name': '审计日志',
                'verbose_name_plural': '审计日志',
            },
        ),
        migrations.AddField(
            model_name='bindhost',
            name='enabled',
            field=models.BooleanField(default=True, verbose_name='是否启用'),
        ),
        migrations.AddField(
            model_name='session',
            name='bind_host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.BindHost', verbose_name='操作的主机'),
        ),
        migrations.AddField(
            model_name='session',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]