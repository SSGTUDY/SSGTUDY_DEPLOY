from django.shortcuts import render

# match.html
def match(request):
    return render(request, 'match.html')

# study_edit.html
def study_edit(request):
    return render(request, 'study_edit.html')

# study_delete.html
def study_delete(request):
    return render(request, 'study_delete.html')

# study_detail.html
def study_detail(request):
    return render(request, 'study_detail.html')