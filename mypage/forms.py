from django import forms
from .models import Hashtag, Recruit
from django_summernote.widgets import SummernoteWidget

class RecruitForm(forms.ModelForm):
    class Meta:
        model = Recruit
        fields = ['recruit_field', 'recruit_status', 'recruit_title', 'recruit_period_start', 'recruit_period_end', 'recruit_number', 'recruit_hashtag', 'recruit_meeting', 'recruit_content', 'recruit_image']

        labels = {
            'recruit_field' : '모집분야',
            'recruit_status' : '모집상태',
            'recruit_title' : '글제목',
            'recruit_period_start' : '모집시작',
            'recruit_period_end' : '모집종료',
            'recruit_number' : '모집인원',
            'recruit_hashtag' : '해시태그',
            'recruit_meeting' : '대면여부',
            'recruit_content' : '글내용',
            'recruit_image' : '이미지',
        }

        widgets = {
            'recruit_content': SummernoteWidget(),
            'recruit_period_start' : forms.DateInput(format=('%m-%d-%Y') , attrs = {'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'recruit_period_end' : forms.DateInput(format=('%m-%d-%Y') , attrs = {'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'})
        }

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['hashtag']