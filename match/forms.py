from django import forms
from .models import Comment, ReComment, RecruitUser

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_content']

        labels = {
            'comment_content': '댓글작성'
        }

class ReCommentForm(forms.ModelForm):
    class Meta:
        model = ReComment
        fields = ['recomment_content']

        labels = {
            'recomment_content': '답글작성'
        }

class RecruitUserForm(forms.ModelForm):
    class Meta:
        model = RecruitUser
        exclude = ('recruit_user_id', 'recruit_user_register')