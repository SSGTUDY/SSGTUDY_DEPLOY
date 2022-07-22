from django.shortcuts import render

# match.html
def match(request):
    return render(request, 'match.html')

def study_detail(request):
    return render(request, 'study_detail.html')