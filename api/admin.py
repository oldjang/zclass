from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(UserInformation)
admin.site.register(ClassInformation)
admin.site.register(StudentClassInformation)
admin.site.register(FileInformation)
admin.site.register(QuestionInformation)
admin.site.register(GroupInformation)
admin.site.register(BoardInformation)
admin.site.register(CommentInformation)
