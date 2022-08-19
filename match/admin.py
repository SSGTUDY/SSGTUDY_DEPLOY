from django.contrib import admin
from .models import Comment, ReComment, RecruitUser
# Register your models here.
admin.site.register(Comment)
admin.site.register(ReComment)
admin.site.register(RecruitUser)