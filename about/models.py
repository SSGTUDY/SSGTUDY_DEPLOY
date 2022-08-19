from django.db import models
from home.models import User

# Create your models here.
class Question(models.Model):
    question_writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    question_date = models.DateTimeField(auto_now_add=True, blank=True)
    question_title = models.CharField(max_length=100)
    question_content = models.TextField()
    question_image = models.ImageField(upload_to='questions/', null=True, blank = True)

    def __str__(self):
        return self.question_title

class QuestionComment(models.Model):
    question_comment_question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name = 'question_comments')
    question_comment_writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'question_comments')
    question_comment_date = models.DateTimeField(auto_now_add=True)
    question_comment_content = models.CharField(max_length=1000)

    def __str__(self):
        return self.question_comment_content
