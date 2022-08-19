from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RecruitForm
from .models import Bookmark, Recruit
from django.utils import timezone

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
            return redirect('study_detail', recruit.id)
    else:
        form = RecruitForm(instance = recruit)
        return render(request, 'study_register.html', {'form': form})

# study_list.html
@login_required
def study_list(request):
    recruits = Recruit.objects
    return render(request, 'study_list.html', {'recruits': recruits})

# study_bookmark.html
@login_required
def study_bookmark(request):
    bookmarks = Bookmark.objects
    return render(request, 'study_bookmark.html', {'bookmarks': bookmarks})
    
# study_schedule.html
def study_schedule(request):
    return render(request, 'study_schedule.html')

# mypage_edit.html
def mypage_edit(request):
    return render(request, 'mypage_edit.html')