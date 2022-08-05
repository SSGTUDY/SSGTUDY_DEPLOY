from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm

class UserForm(forms.ModelForm):
    password = forms.CharField(label = '비밀번호', widget = forms.PasswordInput)
    re_password = forms.CharField(label = '비밀번호 재확인', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 're_password', 'nickname', 'phone_number', 'profile_image']

        labels = {
            'username': 'ID',
            'nickname': 'Nickname',
            'phone_number': '전화번호',
            'profile_image': '프로필 사진',
        }

    def clean_re_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['re_password']:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')
        
        return cd['re_password']

class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': (
            "비밀번호나 이메일이 올바르지 않습니다. 다시 확인해 주세요."
        ),
        'inactive': ("이 계정은 인증되지 않았습니다. 인증을 먼저 진행해 주세요."),
    }

    def __init__(self, request=None, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs) # 꼭 있어야 한다!
        self.fields['username'].label = '아이디'    # 수정
        self.fields['password'].label = '비밀번호'
    