from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Question
from .forms import QuestionCommentForm, QuestionForm

# about_main.html
def about_main(request):
    return render(request, 'about_main.html')

# about_manual.html
def about_manual(request):
    return render(request, 'about_manual.html')

# about_notice.html
def about_notice(request):
    return render(request, 'about_notice.html')

def about_qna(request):
    questions = Question.objects
    return render(request, 'about_qna.html', {'questions': questions})

@login_required
def about_qna_write(request):
    if request.method == 'POST':
        question_form = QuestionForm(request.POST, request.FILES)
        if question_form.is_valid():
            question = question_form.save(commit = False)
            question.question_writer = request.user
            question.question_date = timezone.now()
            question.save()
            return redirect('about_qna_detail', question.id)
    else:
        question_form = QuestionForm()
    return render(request, 'about_qna_write.html', {'question_form': question_form})

def about_qna_detail(request, id):
    question = Question.objects.get(id = id)
    if request.method == 'POST':
        question_comment_form = QuestionCommentForm(request.POST)
        if question_comment_form.is_valid():
            question_comment = question_comment_form.save(commit = False)
            question_comment.question_comment_question = question
            question_comment.question_comment_writer = request.user
            question_comment.question_comment_date = timezone.now()
            question_comment.question_comment_content = question_comment_form.cleaned_data['question_comment_content']
            question_comment_form.save()
            return redirect('about_qna_detail', id)
    else:
        question_comment_form = QuestionCommentForm()
    return render(request, 'about_qna_detail.html', {'question': question, 'question_comment_form': question_comment_form})

def about_qna_edit(request, id):
    question = get_object_or_404(Question, id = id)
    if request.method == 'POST':
        question_form = QuestionForm(request.POST, request.FILES, instance = question)
        if question_form.is_valid():
            question = question_form.save(commit = False)
            question.question_date = timezone.now()
            question.save()
            return redirect('about_qna_detail', id)
    else:
        question_form = QuestionForm(instance = question)
    return render(request, 'about_qna_edit.html', {'question_form': question_form})

def about_qna_delete(request, id):
    question = get_object_or_404(Question, id = id)
    question.delete()
    return redirect('about_qna')