from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=256, primary_key=True)
    password = models.CharField(max_length=256)
    user_nickname = models.CharField(max_length=256)


class UserInformation(models.Model):
    user_id = models.CharField(max_length=256, primary_key=True)
    real_name = models.CharField(max_length=256)
    phone_num = models.CharField(max_length=256, null=True)
    email = models.CharField(max_length=256, null=True)
    school = models.CharField(max_length=256, null=True)
    faculty = models.CharField(max_length=256, null=True)
    sex = models.CharField(max_length=256)
    age = models.IntegerField()
    status = models.CharField(max_length=256, default="S")


class ClassInformation(models.Model):
    course_id = models.CharField(max_length=256, primary_key=True)
    admin_id = models.CharField(max_length=256)
    course_name = models.CharField(max_length=256)
    start_data = models.CharField(max_length=256)
    start_time = models.CharField(max_length=256)
    during_time = models.IntegerField()
    detail = models.CharField(max_length=65536, null=True)


class StudentClassInformation(models.Model):
    student_id = models.CharField(max_length=256)
    course_id = models.CharField(max_length=256)


class FileInformation(models.Model):
    doc_id = models.CharField(max_length=256, primary_key=True)
    course_id = models.CharField(max_length=256)
    doc_name = models.CharField(max_length=256)
    doc_data = models.CharField(max_length=65536)


class QuestionInformation(models.Model):
    ques_id = models.CharField(max_length=256, primary_key=True)
    student_id = models.CharField(max_length=256)
    course_id = models.CharField(max_length=256)
    create_time = models.CharField(max_length=256)
    ppt_page = models.IntegerField()
    ques_detail = models.CharField(max_length=65536)
    ques_status = models.CharField(max_length=256)


class GroupInformation(models.Model):
    student_id = models.CharField(max_length=256)
    course_id = models.CharField(max_length=256)
    group_id = models.CharField(max_length=256)


class BoardInformation(models.Model):
    whiteboard_id = models.CharField(max_length=256, primary_key=True)
    course_id = models.CharField(max_length=256)
    group_id = models.CharField(max_length=256)
    whiteboard_image = models.CharField(max_length=256,null=True)


class CommentInformation(models.Model):
    comment_id = models.CharField(max_length=256, primary_key=True)
    status = models.CharField(max_length=256)
    whiteboard_id = models.CharField(max_length=256)
    ques_id = models.CharField(max_length=256)
    user_id = models.CharField(max_length=256)
    comment_time = models.CharField(max_length=256)
    comment_detail = models.CharField(max_length=256)
