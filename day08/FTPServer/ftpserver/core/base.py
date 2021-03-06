#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Breakering"
# Date: 2017/5/29
"""基类模块，提供基础功能"""
import os
import pickle
import hashlib
from conf import settings
from core import ftp_server


class BaseClass(object):
    """基类，提供基础功能"""
    def save(self):
        class_name = self.__class__.__name__
        class_to_dir = settings.CLASS_TO_DIR[class_name]
        obj_path = os.path.join(class_to_dir, str(self.id))
        pickle.dump(self, open(obj_path, "wb"))

    @classmethod
    def get_all_obj(cls):
        """
        可以返回一个类生成的所有对象
        :return:
        """
        class_name = cls.__name__
        class_to_dir = settings.CLASS_TO_DIR[class_name]
        obj_list = []
        for file_name in os.listdir(class_to_dir):
            file_path = os.path.join(class_to_dir, file_name)
            obj = pickle.load(open(file_path, "rb"))
            obj_list.append(obj)
        return obj_list

    def enroll(self, username, password):
        """ 注册方法 """
        class_name = self.__class__.__name__
        if class_name in settings.CAN_ENROLL:  # 如过类名在可注册字典里则可以进行注册
            for obj in self.__class__.get_all_obj():  # 通过类名来获取该类生成的所有对象
                if username == obj.username:
                    print("用户名已经存在！")
                    return 650
            self.username = username
            passwd = hashlib.md5()  # 获取md5加密对象
            passwd.update(password.encode())  # 加密password
            self.password = passwd.hexdigest()  # 获取加密后的十六进制格式
            self.save()
            ftp_server.action_logger.info("%s-%s注册了该系统！" % (settings.CAN_ENROLL[class_name], self.username))
            print("\033[31;1m%s-%s注册成功！\033[0m" % (settings.CAN_ENROLL[class_name], self.username))
            return 651
        else:
            return 652

    @classmethod
    def login(cls, username, password):
        status = 653
        obj = None
        class_name = cls.__name__
        passwd = hashlib.md5()  # 获取md5加密对象
        passwd.update(password.encode())  # 加密password
        password = passwd.hexdigest()  # 获取加密后的十六进制格式
        if class_name in settings.CAN_LOGIN:  # 如果类名在可登陆字典里则其可以进行登陆
            obj_list = cls.get_all_obj()  # 通过类名获取该类下的所有对象
            for obj in obj_list:
                if username == obj.username and password == obj.password:
                    status = 654
                    obj = obj
                    ftp_server.action_logger.info("%s-%s登陆了该系统！" % (settings.CAN_ENROLL[class_name], obj.username))
                    return {"status": status, "obj": obj}
        else:
            status = 655
            obj = None
            return {"status": status, "obj": obj}
        return {"status": status, "obj": obj}
