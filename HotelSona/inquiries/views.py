from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from inquiries.models import Question
from django.utils import timezone
from datetime import datetime
from django.core.paginator import Paginator
from django.contrib import messages



def customer_voice(request):
    question_list = Question.objects.order_by('-created_date') # order the questions by created_date
    paginator = Paginator(question_list, 5) # 10 questions per page
    page = request.GET.get('page') # get the current page number from the request's query parameter
    questions = paginator.get_page(page) # get the questions for the current page
    context = {'questions': questions}
    return render(request, 'customer-voice.html', context)


@login_required
def customer_question(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        title = request.POST.get('title')
        content = request.POST.get('content')
        created_date = datetime.now().strftime("%Y-%m-%d") # 현재 시간을 yyyy-mm-dd 형식으로 변경
        question = Question.objects.create(author=author, title=title, content=content, created_date=created_date)
        return redirect('inquiries:customer_voice')
    else:
        return render(request, 'customer-question.html')

def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answer = question.answer
    return render(request, 'question-detail.html', {'question': question, 'answer': answer})