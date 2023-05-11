from django.shortcuts import render, redirect, get_object_or_404
from inquiries.models import Question
from django.utils import timezone
from datetime import datetime




def customer_voice(request):
    questions = Question.objects.order_by('-created_date') # order the questions by created_date
    context = {'questions': questions}
    return render(request, 'customer-voice.html', context)



def customer_question(request):
    if request.method=='POST':
        author = request.POST.get('author')
        title = request.POST.get('title')
        content = request.POST.get('content')
        created_date = datetime.now().strftime("%Y-%m-%d") # 현재 시간을 yyyy-mm-dd 형식으로 변경
        question = Question.objects.create(author=author, title=title, content=content, created_date=created_date)
        return redirect('inquiries:customer_voice')
    else:
        return render(request, 'customer-question.html')
    

def customer_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'customer-detail.html', context)