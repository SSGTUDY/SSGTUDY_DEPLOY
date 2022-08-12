from django.db import models
from home.models import User
from mypage.models import Recruit
# Create your models here.

class Comment(models.Model):
    comment_recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE, related_name = 'comments')
    comment_writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'comments')
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_content = models.CharField(max_length=1000)

    def __str__(self):
        return self.comment_content

class ReComment(models.Model):
    recomment_comment = models.ForeignKey(Comment, on_delete = models.CASCADE, related_name = 'recomments')
    recomment_writer = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'recomments')
    recomment_date = models.DateTimeField(auto_now_add=True)
    recomment_content = models.CharField(max_length=1000)

    def __str__(self):
        return self.recomment_content