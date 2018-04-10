#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from web.service import server


class ServerJsonView(View):

    def __init__(self, **kwargs):
        self.obj = server.Server()
        super(ServerJsonView, self).__init__(**kwargs)

    def get(self, request):
        response = self.obj.fetch_queryset(request)
        return JsonResponse(response.__dict__)

    def delete(self, request):
        response = self.obj.delete_queryset(request)
        return JsonResponse(response.__dict__)

    def put(self, request):
        response = self.obj.put_queryset(request)
        return JsonResponse(response.__dict__)

    def post(self, request):
        response = self.obj.post_queryset(request)
        return JsonResponse(response.__dict__)


class AddServerView(View):
    def get(self, request, *args, **kwargs):
        service_obj = server.Server()
        model_form_class = service_obj.create_model_form()
        model_form_obj = model_form_class()
        return render(request, 'add_server.html', {
            "model_form_obj": model_form_obj,
            "service_obj": service_obj
        })
