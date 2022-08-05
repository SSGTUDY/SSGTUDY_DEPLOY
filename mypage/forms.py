from django import forms
from .models import Hashtag, Recruit
from django_summernote.widgets import SummernoteWidget
from home.forms import UserForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import  UserChangeForm

class RecruitForm(forms.ModelForm):
    class Meta:
        model = Recruit
        fields = ['recruit_field', 'recruit_status', 'recruit_title', 'recruit_period_start', 'recruit_period_end', 'recruit_number', 'recruit_meeting', 'recruit_content', 'recruit_image']

        labels = {
            'recruit_field' : '모집분야',
            'recruit_status' : '모집상태',
            'recruit_title' : '글제목',
            'recruit_period_start' : '모집시작',
            'recruit_period_end' : '모집종료',
            'recruit_number' : '모집인원',
            'recruit_meeting' : '대면여부',
            'recruit_content' : '글내용',
            'recruit_image' : '이미지',
        }

        widgets = {
            'recruit_field': forms.RadioSelect(),
            'recruit_status': forms.RadioSelect(),
            'recruit_meeting': forms.RadioSelect(),
            'recruit_content': SummernoteWidget(),
            'recruit_period_start' : forms.DateInput(attrs = {'placeholder': 'Select a date', 'type': 'date'}),
            'recruit_period_end' : forms.DateInput(attrs = {'placeholder': 'Select a date', 'type': 'date'})
        }

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['hashtag_content']

        labels = {
            'hashtag_content': '해시태그'
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username','nickname']

class CustomerMediaChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['profile_image']

