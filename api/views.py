import os
import time

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView

from zclass.settings import BASE_DIR
from .models import *
from .seializers import *


# Create your views here.

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        # 设置一个默认的返回参数
        ret = {'code': 1000, 'msg': None}
        print("OK")
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username, password=password).first()
        if not user:
            ret['code'] = '1001'
            ret['msg'] = '用户名或者密码错误'
            return JsonResponse(ret)

        ret['msg'] = '登录成功'
        ret["userid"] = user.user_id
        return JsonResponse(ret)


class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': None}
        username = request.data.get('username')
        password = request.data.get('password')
        obj = User.objects.filter(username=username).first()
        if obj:
            ret['code'] = '1001'
            ret['msg'] = '用户名已被注册'
            return JsonResponse(ret)

        user = User(username=username, password=password, user_id=str(int(time.time())))
        user.save()
        ret['msg'] = '注册成功'
        ret["userid"] = user.user_id
        return JsonResponse(ret)


class UploadView(APIView):
    def post(self, request):
        ret = {'code': 1000, 'msg': None}
        file = request.FILES.get("file", None)
        if not file:
            ret['code'] = '1002'
            ret['msg'] = '缺少文件'
            return JsonResponse(ret)
        save_file = open(os.path.join(BASE_DIR, 'medias\\' + file.name), 'wb+')
        for chunk in file.chunks():
            save_file.write(chunk)
        save_file.close()
        ret['msg'] = '上传成功'
        ret['url'] = os.path.join(BASE_DIR, 'medias\\' + file.name)
        return JsonResponse(ret)


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserInformation.objects.all()
    serializer_class = UserSerializers


class ClassViewSet(viewsets.ModelViewSet):
    queryset = ClassInformation.objects.all()
    serializer_class = ClassSerializers


class StudentClassViewSet(viewsets.ModelViewSet):
    queryset = StudentClassInformation.objects.all()
    serializer_class = StudentClassSerializers


class FileViewSet(viewsets.ModelViewSet):
    queryset = FileInformation.objects.all()
    serializer_class = FileSerializers


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = QuestionInformation.objects.all()
    serializer_class = QuestionSerializers


class GroupViewSet(viewsets.ModelViewSet):
    queryset = GroupInformation.objects.all()
    serializer_class = GroupSerializers


class BoardViewSet(viewsets.ModelViewSet):
    queryset = BoardInformation.objects.all()
    serializer_class = BoardSerializers


class CommentViewSet(viewsets.ModelViewSet):
    queryset = CommentInformation.objects.all()
    serializer_class = CommentSerializers
