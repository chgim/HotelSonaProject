from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from inquiries.models import Question
from django.utils import timezone
from datetime import datetime
from django.core.paginator import Paginator
from django.contrib import messages


def customer_voice(request):
    question_list = Question.objects.order_by('-created_date')
    paginator = Paginator(question_list, 5) # 페이징
    page = request.GET.get('page')
    questions = paginator.get_page(page)
    context = {'questions': questions}
    return render(request, 'customer-voice.html', context)


@login_required
def customer_question(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        title = request.POST.get('title')
        content = request.POST.get('content')
        created_date = datetime.now().strftime("%Y-%m-%d")
        is_public = request.POST.get('is_public') == 'True'
        question = Question.objects.create(author=author, title=title, content=content, created_date=created_date, is_public=is_public)
        messages.success(request, '질문이 등록되었습니다.')
        return redirect('inquiries:customer_voice')
    else:
        return render(request, 'customer-question.html')

def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if question.is_public: # 공개
        answer = question.answer
        return render(request, 'question-detail.html', {'question': question, 'answer': answer})
    elif not question.is_public and question.author == request.user.username: # 비공개 & 작성자
        answer = question.answer
        return render(request, 'question-detail.html', {'question': question, 'answer': answer})
    else: # 비공개 & 작성자 아님
        messages.error(request, '해당 질문은 비공개되어 있습니다.')
        return redirect('inquiries:customer_voice')
    
    
def delete_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if question.author == request.user.username: # 삭제 버튼을 누른 사람이 작성자일 경우 
        question.delete()
        messages.success(request, '질문이 성공적으로 삭제되었습니다.')
    else: # 삭제 버튼을 누른 사람이 작성자가 아닐경우(애초에 작성자만 삭제 버튼이 보임)
        messages.error(request, '질문 삭제 권한이 없습니다.')
    return redirect('inquiries:customer_voice')