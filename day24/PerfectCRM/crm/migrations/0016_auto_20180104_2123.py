# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-04 13:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0015_menu_icon'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('can_access_sales_index', '可以访问销售首页'), ('can_access_enrollment_for_customer', '可以访问报名页'), ('can_enrollment_for_customer', '可以给用户报名'), ('can_download_identity_photo', '可以下载身份证照片'), ('can_access_contract_detail', '可以查看合同信息'), ('can_reject_contract', '可以驳回合同'), ('can_access_table_index', '可以访问kind_admin下的APP库'), ('can_access_table_objs', '可以访问kind_admin下注册的所有表'), ('can_do_action_or_change_table_objs', '可以对kind_admin下注册的所有表进行行内编辑和action操作'), ('can_access_table_change', '可以访问kind_admin下注册的所有表的对象修改页'), ('can_change_table_obj', '可以修改kind_admin下注册的所有表的对象'), ('can_access_table_delete', '可以访问kind_admin下注册的所有表的删除页'), ('can_delete_all_table_obj', '可以删除kind_admin下注册的所有表的信息'), ('can_access_table_add', '可以访问kind_admin下注册的所有表的增加信息页'), ('can_add_all_table_obj', '可以增加kind_admin下注册的所有表的信息'), ('can_access_customer_table', '可以访问kind_admin下注册的客户库'), ('can_access_customer_add', '可以访问在kind_admin下注册的客户库添加客户页面'), ('can_add_customer', '可以在kind_admin下注册的客户库添加客户'), ('can_access_customer_change', '可以访问在kind_admin下注册的客户库所生成的客户修改页'), ('can_change_customer', '可以修改在kind_admin下注册的客户库中的客户,且只能修改自己的客户'), ('can_access_change_password', '可以访问密码修改页'), ('can_change_own_password', '可以修改自己的密码'), ('can_change_all_password', '可以修改所有人的密码'), ('can_access_customer_followup', '可以访问kind_admin下注册的客户跟进记录'), ('can_access_customer_followup_change', '可以访问kind_admin下注册的客户跟进记录的修改页面'), ('can_change_customer_followup', '可以修改kind_admin下注册的客户跟进记录'), ('can_access_customer_followup_add', '可以访问kind_admin下注册的客户跟进记录的添加页面'), ('can_add_customer_followup', '可以添加kind_admin下注册的客户跟进记录'), ('can_access_course_record', '可以访问kind_admin下注册的上课记录'), ('can_do_action_or_change_course_record', '可以对kind_admin下注册的上课记录进行行内编辑和action操作')), 'verbose_name_plural': '账户表'},
        ),
    ]
