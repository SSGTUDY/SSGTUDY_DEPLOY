from django.shortcuts import render

# main.html
def main(request):
    return render(request, 'main.html')

# login.html
def login(request):
    return render(request, 'login.html')

# logout.html
def logout(request):
    return render(request, 'logout.html')

# signup.html
def signup(request):
    return render(request, 'signup.html')

# signup_end.html
def signup_end(request):
    return render(request, 'signup_end.html')