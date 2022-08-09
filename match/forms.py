from django import forms
from .models import Comment, ReComment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_content']

        labels = {
            'comment_content': '댓글작성',

        }



class ReCommentForm(forms.ModelForm):
    class Meta:
        model = ReComment
        fields = ['recomment_content']

        labels = {
            'recomment_content': '답글작성'
        }