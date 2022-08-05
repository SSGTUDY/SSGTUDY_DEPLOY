from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from mypage.models import Recruit, Hashtag
from mypage.forms import RecruitForm, HashtagForm
from .forms import CommentForm, ReCommentForm
from .models import Comment

# match.html
def match(request):
    recruits = Recruit.objects
    return render(request, 'match.html', {'recruits': recruits})

# study_detail.html
def study_detail(request, id):
    recruit = get_object_or_404(Recruit, id = id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        re_form = ReCommentForm(request.POST)
        hashtag_form = HashtagForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.comment_recruit = recruit
            comment.comment_writer = request.user
            comment.comment_date = timezone.now()
            comment.comment_content = form.cleaned_data['comment_content']
            comment.save()
            return redirect('study_detail', id)
        if re_form.is_valid():
            recomment = re_form.save(commit = False)
            recomment.recomment_comment = comment
            recomment.recomment_writer = request.user
            recomment.recomment_date = timezone.now()
            recomment.recomment_content = form.cleaned_data['recomment_content']
            recomment.save()
        if hashtag_form.is_valid():
            hashtag = hashtag_form.save(commit = False)
            hashtag.hashtag_recruit = recruit
            hashtag.hashtag_content = form.cleaned_data['hashtag_content']
            hashtag_form.save()
            return redirect('study_detail', id)
    else:
        form = CommentForm()
        re_form = ReCommentForm()
        hashtag_form = HashtagForm()
    return render(request, 'study_detail.html', {'recruit': recruit, 'form': form, 're_form': re_form, 'hashtag_form': hashtag_form})

# study_edit.html
@login_required
def study_edit(request, id):
    recruit = get_object_or_404(Recruit, id = id)
    if request.method == 'POST':
        form = RecruitForm(request.POST, request.FILES, instance = recruit)
        if form.is_valid():
            recruit = form.save(commit=False)
            recruit.recruit_date = timezone.now()
            recruit.save()
            return redirect('study_detail', id)
    else:
        form = RecruitForm(instance = recruit)
        return render(request, 'study_edit.html', {'form': form})

# study_delete.html
@login_required
def study_delete(request, id):
    recruit = get_object_or_404(Recruit, id = id)
    recruit.delete()
    return redirect('match')

@login_required
def hashtag_write(request, id):
    recruit = get_object_or_404(Recruit, id = id)
    if request.method == "POST":
        hashtag_form = HashtagForm(request.POST)
        if hashtag_form.is_valid():
            hashtag = hashtag_form.save(commit = False)
            hashtag.hashtag_recruit = recruit
            hashtag.hashtag_writer = request.user
            hashtag.hashtag_date = timezone.now()
            hashtag.save()
            return redirect('study_detail', id)
    else:
        hashtag_form = HashtagForm()
    return render(request, 'study_detail.html')

# 댓글 수정하는 함수
@login_required
def comment_edit(request, comment_id, id):
    # 댓글 아이디를 얻어와 comment_id 변수에 저장
    comment_id = Comment.objects.get(id = comment_id)
    form = CommentForm(instance = comment_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance = comment_id)
        if form.is_valid():
            form.save()
            return redirect('study_detail', id)
    return render (request, 'comment_edit.html', {'form': form})

@login_required
def comment_delete(request, comment_id, id):
    comment_id = Comment.objects.get(id = comment_id)
    comment_id.delete()
    return redirect('study_detail', id)

@login_required
def recomment_write(request, id, comment_id):   
    comment = get_object_or_404(Comment, id = comment_id)
    if request.method == "POST":
        re_form = ReCommentForm(request.POST)
        if re_form.is_valid():
            recomment = re_form.save(commit = False)
            recomment.recomment_comment = comment
            recomment.recomment_writer = request.user
            recomment.recomment_date = timezone.now()
            recomment.save()
            return redirect('study_detail', id)
    else:
        re_form = ReCommentForm()
    return render(request, 'study_detail.html')