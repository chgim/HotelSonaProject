from django.shortcuts import render

# Create your views here.


def mypage_1(request):
    return render(request, 'mypage-1.html')


def mypage_2(request):
    return render(request, 'mypage-2.html')
