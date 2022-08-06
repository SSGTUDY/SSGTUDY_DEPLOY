from django.shortcuts import get_object_or_404, render, redirect
from .forms import RecruitForm
from .models import Recruit
from django.utils import timezone
from django.contrib import auth
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.hashers import check_password
from home.models import User
from django.contrib.auth.forms import UserChangeForm
from .forms import CustomUserChangeForm,ProfileForm
from django.contrib import messages

# mypage_main.html
def mypage_main(request):
    return render(request, 'mypage_main.html')

# study_register.html
def study_register(request, recruit = None):
    if request.method == "POST":
        form = RecruitForm(request.POST, request.FILES, instance = recruit)
        if form.is_valid():
            recruit = form.save(commit = False)
            recruit.recruit_writer = request.user
            recruit.recruit_date = timezone.now()
            recruit.save()
            return redirect('main')
    else:
        form = RecruitForm(instance = recruit)
        return render(request, 'study_register.html', {'form': form})

# study_list.html
def study_list(request):
    return render(request, 'study_list.html')

# study_bookmark.html
def study_bookmark(request):
    return render(request, 'study_bookmark.html')

# study_schedule.html
def study_schedule(request):
    return render(request, 'study_schedule.html')

# mypage_edit.html
def mypage_edit(request):
    return render(request, 'mypage_edit.html')

def logout(request):
    auth.logout(request)
    return redirect('main')

def temp(request):
    return render(request,'re_password.html')


def change_pass(request):
    return render(request,'change_password.html')

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request,'Password was updated!')
            return redirect('mypage_edit')
        else:
            messages.error(request,'Please correct the error')
    else:
        form = PasswordChangeForm(request.user)
    return render(request,'change_password.html',{'form':form})

def change_img(request):
    return render(request,'change_image.html')

def change_nickname(request):
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST,instance=request.user)
        if user_change_form.is_valid():
            user_change_form.save()
            messages.info(request,"회원정보가 변경되었습니다!")
            return redirect('mypage_edit')
    else:
        user_change_form = CustomUserChangeForm(instance=request.user)
        return render(request,'change_nickname.html',{
            'user_change_form':user_change_form
        })

def change_image(request):
    if request.method == 'POST':

        user_change_form = CustomUserChangeForm(request.POST,instance = request.user)
        profile_form = ProfileForm(request.POST,request.FILES,instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('mypage_edit')
    else:
        profile_form = ProfileForm(instance=request.user)
        return render(request,'change_image.html',{
            'profile_form': profile_form
        })



