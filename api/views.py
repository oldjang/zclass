from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView

from .models import *
from .seializers import *


# Create your views here.

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        # 设置一个默认的返回参数
        ret = {'code': 1000, 'msg': None}
        print("OK")
        user_id = request.data.get('user_id')
        password = request.data.get('password')
        obj = User.objects.filter(user_id=user_id, password=password).first()
        if not obj:
            return HttpResponse("OK")
        return HttpResponse("Failed")


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
