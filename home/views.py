from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import UserForm, CustomAuthenticationForm
from mypage.models import Hashtag
from mypage.models import Hashtag, Recruit
from home.models import User
# main.html
def main(request):
    hashtag = Hashtag.objects
    user = User.objects
    return render(request, 'main.html', {'hashtag': hashtag, 'user': user})

# login.html
def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.get_user()
            auth.login(request, new_user)
            return redirect('main')   
        else:
            return render(request, 'login.html', {'form':form})
    else:
        
        form = CustomAuthenticationForm()
        return render(request, 'login.html', {'form':form})

# logout.html
def logout(request):
    auth.logout(request)
    return redirect('main')

# signup.html
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'signup_end.html', {'user':user})
    elif request.method == 'GET':
        form = UserForm()
    return render(request, 'signup.html', {'form': form})

# signup_end.html
def signup_end(request):
    return render(request, 'signup_end.html')

def main(request):
    hashtag = Hashtag.objects
    recruit = Recruit.objects
    user = User.objects
    return render(request, 'main.html', {'hashtag': hashtag, 'recruit': recruit, 'user': user})