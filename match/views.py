from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from mypage.models import Recruit, Hashtag
from home.models import User
from datetime import date, datetime,timedelta
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from mypage.forms import BookmarkForm, RecruitForm, HashtagForm
from .forms import CommentForm, ReCommentForm, RecruitUserForm
from .models import Comment
from django.http import HttpResponse
from django.db.models import Q


def hashtag_detail(request, pk):
    startdate = date.today()
    enddate = startdate + timedelta(days = 1000)
    recruits = Recruit.objects.filter(recruit_period_end__gte = enddate, recruit_status = 'ongoing').order_by('recruit_period_end')
    paginator = Paginator(recruits,5)
    page = request.GET.get('page1')
    recruit_all = Recruit.objects.filter(recruit_period_end__gte = enddate, recruit_status = 'ongoing').order_by('recruit_period_end')
    recruit_top = Recruit.objects.filter(recruit_period_end__lte = enddate,recruit_period_end__gte = startdate, recruit_status = 'ongoing').order_by('recruit_period_end')
    recruit_top = recruit_top[:5]
    try:
        recruits = paginator.page(page)
    except PageNotAnInteger:
        recruits = paginator.page(1)
    except EmptyPage:
        recruits = paginator.page(paginator.num_pages)

    hashtag = Hashtag.objects
    hashtags = get_object_or_404(Hashtag, pk = pk)
    hashtag_recruits = hashtags.recruit_set

    recruit_field_study = Recruit.objects.filter(recruit_field="study",recruit_status = 'ongoing').order_by('recruit_period_end')
    recruit_field_club = Recruit.objects.filter(recruit_field="club",recruit_status = 'ongoing').order_by('recruit_period_end')
    recruit_field_project = Recruit.objects.filter(recruit_field="project",recruit_status = 'ongoing').order_by('recruit_period_end')
    recruit_field_survey = Recruit.objects.filter(recruit_field="survey",recruit_status = 'ongoing').order_by('recruit_period_end')
    print(recruit_top)
    q = request.GET.get('q', '')
    if q:
        recruit_all = recruit_all.filter(Q(recruit_title__icontains=q) | Q(recruit_content__icontains=q))
    
    return render(request, 'match.html', {'posts':recruits,'hashtag':hashtag, 'hashtags': hashtags, 'hashtag_recruits': hashtag_recruits,
        'recruit_field_study': recruit_field_study, 'recruit_field_club': recruit_field_club, 'recruit_field_project': recruit_field_project, 'recruit_field_survey': recruit_field_survey,
        'q': q,'recruit_all':recruit_all,'recruit_top':recruit_top})

# study_detail.html
def study_detail(request, id):
    recruit = get_object_or_404(Recruit, id = id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        re_form = ReCommentForm(request.POST)
        hashtag_form = HashtagForm(request.POST)
        recruit_user_form = RecruitUserForm(request.POST)
        bookmark_form = BookmarkForm(request.POST)
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
        if recruit_user_form.is_valid():
            recruit_user = recruit_user_form.save(commit = False)
            recruit_user.recruit_user_id = recruit
            recruit_user.recruit_user_register = request.user
            recruit_user.save()
            return redirect('study_detail', id)
        if bookmark_form.is_valid():
            bookmark = bookmark_form.save(commit = False)
            bookmark.bookmark_id = recruit
            bookmark.bookmark_user = request.user
            bookmark.save()
            return redirect('study_detail', id)
    else:
        form = CommentForm()
        re_form = ReCommentForm()
        hashtag_form = HashtagForm()
        recruit_user_form = RecruitUserForm()
        bookmark_form = BookmarkForm()

    return render(request, 'study_detail.html',
    {'recruit': recruit, 'form': form, 're_form': re_form, 'hashtag_form': hashtag_form, 'recruit_user_form': recruit_user_form, 'bookmark_form': bookmark_form})

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
    hashtag_form = HashtagForm(request.POST)
    if request.method == "POST":
        if hashtag_form.is_valid():
            hashtag = hashtag_form.save(commit = False)
            hashtag, created = Hashtag.objects.get_or_create(hashtag_content = hashtag.hashtag_content)
            recruit.recruit_hashtag.add(hashtag)
            return redirect('study_detail', id)
    else:
        hashtag_form = HashtagForm()
    return render(request, 'study_detail.html',{'recruit':recruit})

# 가입 신청
@login_required
def recruit_user(request, id):
    recruit = get_object_or_404(Recruit, id = id)
    if request.method == "POST":
        recruit_user_form = RecruitUserForm(request.POST)
        if recruit_user_form.is_valid():
            recruit_user = recruit_user_form.save(commit = False)
            recruit_user.recruit_user_id = recruit
            recruit_user.recruit_user_register = request.user
            recruit_user.save()
            return HttpResponse("<script> window.close();</script>");
    else:
        recruit_user_form = RecruitUserForm()
    return render(request, 'request_user.html')

@login_required
def bookmark(request, id):
    recruit = get_object_or_404(Recruit, id = id)
    if request.method == "POST":
        bookmark_form = BookmarkForm(request.POST)
        if bookmark_form.is_valid():
            bookmark = bookmark_form.save(commit = False)
            bookmark.bookmark_id = recruit
            bookmark.bookmark_user = request.user
            bookmark.save()
            return redirect('study_detail', id)
    else:
        bookmark_form = BookmarkForm()
    return render(request, 'request_user.html')

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




def find_date_end(request):
    #전체 게시글에 대한 함수들 (페이지네이션도 전체 게시글 대상)
   startdate = date.today()
   enddate = startdate + timedelta(days = 1000)
   recruits = Recruit.objects.filter(recruit_period_end__lte = enddate,recruit_period_end__gte = startdate, recruit_status = 'ongoing').order_by('recruit_period_end')
   recruit_top = Recruit.objects.filter(recruit_period_end__lte = enddate,recruit_period_end__gte = startdate, recruit_status = 'ongoing').order_by('recruit_period_end')
   recruit_top = recruit_top[:5]
   recruit_all = Recruit.objects.filter(recruit_period_end__lte = enddate, recruit_period_end__gte = startdate, recruit_status = 'ongoing').order_by('recruit_period_end')
   
   
   hashtag = Hashtag.objects
   
   #스터디에 대한 코드(스터디에 대한 페이지네이션)
   
   recruit_field_study = Recruit.objects.filter(recruit_field="study",recruit_status = 'ongoing').order_by('recruit_period_end')
   
      
   recruit_field_club = Recruit.objects.filter(recruit_field="club",recruit_status = 'ongoing').order_by('recruit_period_end')
   recruit_field_project = Recruit.objects.filter(recruit_field="project",recruit_status = 'ongoing').order_by('recruit_period_end')
   recruit_field_survey = Recruit.objects.filter(recruit_field="survey",recruit_status = 'ongoing').order_by('recruit_period_end')
   

   q = request.GET.get('q', '')
   if q:
       recruit_all = recruit_all.filter(Q(recruit_title__icontains=q) | Q(recruit_content__icontains=q))
       
   recruits = recruit_all
   paginator = Paginator(recruits,5)
   page = request.GET.get('page1',1)
   try:
       recruits = paginator.page(page)
   except PageNotAnInteger:
       recruits = paginator.page(1)
   except EmptyPage:
       recruits = paginator.page(paginator.num_pages)
    
    #study페이지네이션
    
   
    
    
       
   return render(request, 'match.html', {'posts':recruits,'hashtag':hashtag,'recruit_field_study': recruit_field_study, 'recruit_field_club': recruit_field_club, 'recruit_field_project': recruit_field_project, 'recruit_field_survey': recruit_field_survey,
    'q': q,'recruit_all':recruit_all,'recruit_top':recruit_top})

@login_required
def likes(request, recruit_id):
    recruit = get_object_or_404(Recruit, id = recruit_id)
    if request.user in recruit.like.all():
        recruit.like.remove(request.user)
        recruit.like_count -= 1
        recruit.save()
    else:
        recruit.like.add(request.user.id)
        recruit.like_count += 1
        recruit.save()

    return redirect('/match/study_detail/' + str(recruit_id))


def sort_by_like(request):
    startdate = date.today()
    enddate = startdate + timedelta(days=200)
    recruits = Recruit.objects.filter(recruit_period_end__lte = enddate, recruit_status = 'ongoing').order_by('-like_count')
    paginator = Paginator(recruits, 5)
    page = request.GET.get('page1')
    recruit_all = Recruit.objects.filter(recruit_period_end__lte=enddate, recruit_status='ongoing').order_by('-like_count')
    try:
        recruits = paginator.page(page)
    except PageNotAnInteger:
        recruits = paginator.page(1)
    except EmptyPage:
        recruits = paginator.page(paginator.num_pages)
    # hashtag = Hashtag.objects.all()
    hashtag = Hashtag.objects.all()
    recruit_field_study = Recruit.objects.filter(recruit_field="study", recruit_status='ongoing').order_by('-like_count')
    recruit_field_club = Recruit.objects.filter(recruit_field="club", recruit_status='ongoing').order_by('-like_count')
    recruit_field_project = Recruit.objects.filter(recruit_field="project", recruit_status='ongoing').order_by('-like_count')
    recruit_field_survey = Recruit.objects.filter(recruit_field="survey", recruit_status='ongoing').order_by('-like_count')

    q = request.GET.get('q', '')
    
    recruit_top = Recruit.objects.filter(recruit_period_end__lte = enddate,recruit_period_end__gte = startdate, recruit_status = 'ongoing').order_by('recruit_period_end')
    recruit_top = recruit_top[:5]

    if q:
        recruit_all = recruit_all.filter(Q(recruit_title__icontains=q) | Q(recruit_content__icontains=q))
    return render(request, 'match.html',
                  {'posts': recruits, 'Posts': hashtag, 'recruit_field_study': recruit_field_study,
                   'recruit_field_club': recruit_field_club, 'recruit_field_project': recruit_field_project,
                   'recruit_field_survey': recruit_field_survey,
                   'q': q, 'recruit_all': recruit_all,'recruit_top':recruit_top, 'hashtag':hashtag})

