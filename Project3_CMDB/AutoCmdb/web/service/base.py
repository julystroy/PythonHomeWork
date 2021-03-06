#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
from django.db.models import Q
from utils.response import BaseResponse
from utils.pager import PageInfo
from django.http.request import QueryDict
from django.forms import ModelForm


class BaseServiceList(object):

    def __init__(
        self,
        condition_config,
        table_config, extra_select,
        global_dict, queryset,
        exclude_fields
    ):
        # 查询条件的配置，列表
        self.condition_config = condition_config

        # 表格的配置，列表
        """
        {
            'q': 'title',       # 用于数据库查询的字段，即Model.Tb.objects.xxx.values(*['v',]), None则表示不获取相应的数据库列
            'title': '标题',     # table表格显示的列名
            'display': 0        # 实现在表格中显示 0，不显示；1显示
            # 表格的每一个td中显示的内容,一个@表示获取数据库查询字段，两个@@，表示根据当前id在全局变量中找到id对应的内容
            'text': {'content': "{id}", 'kwargs': {'id': '@id'}}, 
            'attr': {}          # 自定义属性
        }
        """
        self.table_config = table_config

        # 额外搜索条件，字典
        self.extra_select = extra_select

        # 给前端的全局面临
        self.global_dict = global_dict

        # queryset对象
        self.queryset = queryset

        # 要排除的字段
        self.exclude_fields = exclude_fields

    @property
    def values_list(self):
        """
        数据库查询时的指定字段
        :return:
        """
        values = []
        for item in self.table_config:
            if item['q']:
                values.append(item['q'])
        return values

    @staticmethod
    def queryset_condition(request):
        con_str = request.GET.get('condition', None)
        if not con_str:
            con_dict = {}
        else:
            con_dict = json.loads(con_str)

        con_q = Q()
        for k, v in con_dict.items():
            temp = Q()
            temp.connector = 'OR'
            for item in v:
                temp.children.append((k, item))
            con_q.add(temp, 'AND')

        return con_q

    def fetch_queryset(self, request):
        response = BaseResponse()
        try:
            ret = {}
            conditions = self.queryset_condition(request)
            queryset_count = self.queryset.filter(conditions).count()
            page_info = PageInfo(request.GET.get(
                'pager', None), queryset_count)
            queryset_list = self.queryset.filter(conditions).extra(select=self.extra_select).values(
                *self.values_list)[page_info.start:page_info.end]

            ret['table_config'] = self.table_config
            ret['condition_config'] = self.condition_config
            ret['data_list'] = list(queryset_list)
            ret['page_info'] = {
                "page_str": page_info.pager(),
                "page_start": page_info.start,
            }
            ret['global_dict'] = self.global_dict
            response.data = ret
            response.message = '获取成功'
        except Exception as e:
            response.status = False
            response.message = str(e)

        return response

    def delete_queryset(self, request):
        response = BaseResponse()
        try:
            delete_dict = QueryDict(request.body, encoding='utf-8')
            id_list = delete_dict.getlist('id_list')
            self.queryset.filter(id__in=id_list).delete()
            response.message = '删除成功'
        except Exception as e:
            response.status = False
            response.message = str(e)
        return response

    def put_queryset(self, request):
        response = BaseResponse()
        try:
            response.error = []
            put_dict = QueryDict(request.body, encoding='utf-8')
            update_list = json.loads(put_dict.get('update_list'))
            error_count = 0
            for row_dict in update_list:
                nid = row_dict.pop('nid')
                num = row_dict.pop('num')
                try:
                    self.queryset.filter(id=nid).update(**row_dict)
                except Exception as e:
                    response.error.append({'num': num, 'message': str(e)})
                    response.status = False
                    error_count += 1
            if error_count:
                response.message = '共%s条,失败%s条' % (
                    len(update_list), error_count,)
            else:
                response.message = '更新成功'
        except Exception as e:
            response.status = False
            response.message = str(e)
        return response

    def post_queryset(self, request):
        response = BaseResponse()
        model_form_class = self.create_model_form()
        model_form_obj = model_form_class(request.POST)
        if model_form_obj.is_valid():
            model_form_obj.save()
            response.message = '创建成功'
        else:
            response.status = False
            response.error = model_form_obj.errors
        return response

    def create_model_form(self):

        def __new__(cls, *args, **kwargs):
            for field_name, field_obj in cls.base_fields.items():
                model_field_obj = self.queryset.model._meta.get_field(
                    field_name)
                if type(model_field_obj).__name__ == "DateField":
                    field_obj.widget.attrs["class"] = "form-control date-picker"
                else:
                    field_obj.widget.attrs["class"] = "form-control"
            return ModelForm.__new__(cls)

        class Meta:
            model = self.queryset.model
            fields = "__all__"
            exclude = self.exclude_fields

        attrs = {"Meta": Meta, "__new__": __new__}
        model_form_class = type("DynamicModelForm", (ModelForm,), attrs)
        return model_form_class
