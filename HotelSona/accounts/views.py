from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def register_view(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["email"], password=request.POST["password1"])
            auth.login(request, user)
            return redirect('booking:index')
        return render(request, 'register.html')
    
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
            return redirect('booking:index')
        else:
            return render(request, 'login.html', {'error': '이메일 또는 비밀번호가 올바르지 않습니다.'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('booking:index')