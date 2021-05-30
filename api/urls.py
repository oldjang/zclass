from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from api.views import *

route = routers.DefaultRouter()

# 注册新的路由地址
route.register(r'user', UserViewSet)
route.register(r'class', ClassViewSet)
route.register(r'studentclass', StudentClassViewSet)
route.register(r'file', FileViewSet)
route.register(r'question', QuestionViewSet)
route.register(r'group', GroupViewSet)
route.register(r'board', BoardViewSet)
route.register(r'comment', CommentViewSet)

urlpatterns = [
    url(r'^login/$', LoginView.as_view()),
    url(r'^register/$', RegisterView.as_view()),
    url(r'^upload/$', UploadView.as_view()),
    url('', include(route.urls)),
]
