from django.shortcuts import render

# mypage_main.html
def mypage_main(request):
    return render(request, 'mypage_main.html')

# study_register.html
def study_register(request):
    return render(request, 'study_register.html')

# study_edit.html
def study_edit(request):
    return render(request, 'study_edit.html')

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