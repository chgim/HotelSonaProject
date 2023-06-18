from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

from django.core.exceptions import ValidationError

# Create your views here.

# def register_view(request):
#     if request.method == "POST":
#         if request.POST["password1"] == request.POST["password2"]:
#             user = User.objects.create_user(
#                 username=request.POST["email"], password=request.POST["password1"])
#             auth.login(request, user)
#             messages.info(request, '회원가입 완료')
#             return redirect('booking:index')
#         return render(request, 'register.html')
    
#     return render(request, 'register.html')

# 수정
def register_view(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            email = request.POST["email"]
            # 중복된 이메일인지 확인
            try:
                User.objects.get(username=email)
                # 중복된 이메일이 있는 경우
                messages.error(request, '중복된 이메일입니다. 다른 이메일을 사용해주세요.')
                return redirect('accounts:register_view')
            except User.DoesNotExist:
                # 중복된 이메일이 없는 경우, 회원가입 진행
                user = User.objects.create_user(username=email, password=request.POST["password1"])
                
                messages.info(request, '회원가입 완료')
                return redirect('booking:index')
        else:
            messages.error(request, '비밀번호가 일치하지 않습니다.')
    
    return render(request, 'register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # 로그인 성공 시 추가 동작 수행
            # return render(request, 'booking:index', {'success': '로그인이 성공했습니다.'})
            messages.info(request, '로그인 완료')
            return redirect('booking:index')
        else:
            return render(request, 'login.html', {'error': '이메일 또는 비밀번호가 올바르지 않습니다.'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('booking:index')