from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from accounts.models import UserProfile
from django.core.exceptions import ValidationError
from django.http import HttpResponse
import requests
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


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
                user = User.objects.create_user(
                    username=email, password=request.POST["password1"])
                # 프로필 정보 저장
                name = request.POST["name"]
                birthdate = request.POST["birth"]
                phonenumber = request.POST["cellPhone"]
                UserProfile.objects.create(
                    user=user, name=name, birthdate=birthdate, phonenumber=phonenumber)
                messages.info(request, '회원가입 완료')
                return redirect('booking:index')
        else:
            messages.error(request, '비밀번호가 일치하지 않습니다.')

    return render(request, 'register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # print("A")
            # # 카카오 로그인 시 사용자 정보 동기화
            # if 'kakao' in request.GET.get('provider', ''):
            #     print("B")
            #     # 카카오 액세스 토큰 받아오기
            #     kakao_access_token = get_kakao_access_token(request)

            #     # 사용자 정보를 세션에 저장
            #     request.session['user_id'] = user.id
            #     request.session['user_email'] = user.email
            #     request.session['kakao_access_token'] = kakao_access_token

            #     # 디버그용 출력
            #     print("kakao_access_token:", kakao_access_token)

            messages.info(request, '로그인 완료')
            return redirect('booking:index')
        else:
            return render(request, 'login.html', {'error': '이메일 또는 비밀번호가 올바르지 않습니다.'})
    else:
        return render(request, 'login.html')


# def get_kakao_access_token(request):
#     # 카카오 액세스 토큰을 받아오기 위한 요청을 수행합니다.
#     kakao_token_url = 'https://kauth.kakao.com/oauth/token'
#     # 카카오 개발자 설정에서 발급 받은 클라이언트 아이디로 대체하세요.
#     client_id = '12621d77e02216847e1863225f7edd5d'
#     # 카카오 개발자 설정에 등록한 리다이렉트 URI로 대체하세요.
#     redirect_uri = 'http://127.0.0.1:8000/accounts/kakao/login/callback/'
#     code = request.GET.get('code', '')
#     payload = {
#         'grant_type': 'authorization_code',
#         'client_id': client_id,
#         'redirect_uri': redirect_uri,
#         'code': code,
#     }
#     response = requests.post(kakao_token_url, data=payload)

#     if response.status_code == 200:
#         # 요청이 성공하면 액세스 토큰을 파싱하여 반환합니다.
#         return response.json().get('access_token')
#     else:
#         # 요청이 실패한 경우 예외 처리를 해야 합니다.
#         # 오류 처리 로직 작성
#         pass


# def sync_kakao_user_info(request, access_token):
#     # 카카오 사용자 정보를 동기화하는 요청을 수행합니다.
#     kakao_user_info_url = 'https://kapi.kakao.com/v2/user/me'
#     headers = {
#         'Authorization': f'Bearer {access_token}'
#     }
#     response = requests.get(kakao_user_info_url, headers=headers)

#     if response.status_code == 200:
#         # 요청이 성공하면 카카오 사용자 정보를 파싱하여 세션에 저장하거나 사용자 프로필을 업데이트합니다.
#         kakao_user_info = response.json()
#         kakao_user_id = kakao_user_info.get('id')
#         kakao_user_email = kakao_user_info.get(
#             'kakao_account', {}).get('email')

#         # 사용자 정보를 세션에 저장하거나 사용자 프로필을 업데이트하는 로직을 작성합니다.
#         # ...

#     else:
#         # 요청이 실패한 경우 예외 처리를 해야 합니다.
#         # 오류 처리 로직 작성
#         pass


# def kakao_login_view(request):
#     # 카카오 로그인 후 돌아올 URL(next_url) 가져오기
#     next_url = request.GET.get('next', None)
#     if next_url:
#         # 카카오 로그인 URL 생성 및 리다이렉트
#         kakao_login_url = 'https://kauth.kakao.com/oauth/authorize?client_id=12621d77e02216847e1863225f7edd5d&redirect_uri=http://127.0.0.1:8000/accounts/kakao/login/callback/&response_type=code&scope=profile'
#         return redirect(kakao_login_url)


# def kakao_login_callback_view(request):
#     # 카카오 로그인 콜백 뷰에서는 카카오 로그인 성공 여부를 확인하고,
#     # 성공 시 로그인 뷰로 이동시킵니다.
#     code = request.GET.get('code')
#     if code:
#         access_token = get_kakao_access_token(request, code)
#         if access_token:
#             # 카카오 로그인이 성공한 경우 로그인 뷰로 이동시킵니다.
#             sync_kakao_user_info(request, access_token)
#             return redirect('accounts:login_view')

#     # 카카오 로그인이 실패한 경우 다른 처리 로직을 추가할 수 있습니다.
#     # ...

#     # 실패 시 로그인 페이지로 이동하거나, 에러 메시지를 출력할 수 있습니다.
#     messages.error(request, '카카오 로그인에 실패하였습니다.')
#     return redirect('accounts:login_view')


# def kakao_logout_view(request):
#     if 'kakao_access_token' in request.session:
#         kakao_access_token = request.session['kakao_access_token']
#         kakao_logout_url = 'https://kapi.kakao.com/v1/user/logout'
#         headers = {
#             'Authorization': f'Bearer {kakao_access_token}'
#         }
#         response = requests.post(kakao_logout_url, headers=headers)

#         if response.status_code == 200:
#             # 카카오 로그아웃 성공 시, 세션에 저장된 카카오 액세스 토큰 제거
#             del request.session['kakao_access_token']

#     # 로컬 로그아웃 처리
#     auth_logout(request)
#     return redirect('booking:index')


def logout(request):
    # if 'kakao_access_token' in request.session:
    #     # 카카오 로그아웃 처리
    #     kakao_access_token = request.session['kakao_access_token']
    #     kakao_logout_url = 'https://kapi.kakao.com/v1/user/logout'
    #     headers = {
    #         'Authorization': f'Bearer {kakao_access_token}'
    #     }
    #     response = requests.post(kakao_logout_url, headers=headers)

    #     if response.status_code == 200:
    #         # 카카오 로그아웃 성공 시, 세션에 저장된 카카오 액세스 토큰 제거
    #         del request.session['kakao_access_token']

    # 로컬 로그아웃 처리
    auth_logout(request)
    return redirect('booking:index')
