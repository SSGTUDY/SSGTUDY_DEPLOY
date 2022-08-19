from django import forms
from .models import Question, QuestionComment
from django_summernote.widgets import SummernoteWidget

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_title', 'question_content', 'question_image']

        labels = {
            'question_title': 'QnA 제목',
            'question_content': 'QnA 내용',
            'question_image': 'QnA 이미지',
        }

        widgets = {
            'question_content': SummernoteWidget()
        }

class QuestionCommentForm(forms.ModelForm):
    class Meta:
        model = QuestionComment
        fields = ['question_comment_content']

        labels = {
            'question_comment_content': '답변 작성'
        }