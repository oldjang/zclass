from rest_framework import serializers
from .models import *


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserInformation
        fields = "__all__"


class ClassSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClassInformation
        fields = "__all__"


class StudentClassSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentClassInformation
        fields = "__all__"


class FileSerializers(serializers.ModelSerializer):
    class Meta:
        model = FileInformation
        fields = "__all__"


class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = QuestionInformation
        fields = "__all__"


class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = GroupInformation
        fields = "__all__"


class BoardSerializers(serializers.ModelSerializer):
    class Meta:
        model = BoardInformation
        fields = "__all__"


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = CommentInformation
        fields = "__all__"
