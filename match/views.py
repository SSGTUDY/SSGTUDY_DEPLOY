from django.shortcuts import render

# match.html
def match(request):
    return render(request, 'match.html')