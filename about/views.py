from django.shortcuts import render
# about_main.html
def about_main(request):
    return render(request, 'about_main.html')

# about_manual.html
def about_manual(request):

    return render(request, 'about_manual.html')

# about_post.html
def about_post(request):
    return render(request, 'about_post.html')

# about_notice.html
def about_notice(request):

    return render(request, 'about_notice.html')

# about_qna.html
def about_qna(request):
    return render(request, 'about_qna.html') 