from django.contrib.auth.decorators import login_required
from booking.models import Reservation

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from accounts.forms import UserProfileForm
from accounts.models import UserProfile
from allauth.socialaccount.models import SocialAccount
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.utils import timezone

@login_required
def mypage_1(request):
    reservations = Reservation.objects.filter(user=request.user).order_by('-created_at')
    # 현재 날짜 정보를 계산하여 템플릿으로 전달
    current_date = timezone.now().date()
    # # 카카오 로그인 여부 확인을 위해 변수 추가
    # is_kakao_user = False
    # kakao_account = request.user.socialaccount_set.filter(provider='kakao').first()
    # if kakao_account:
    #     is_kakao_user = True
    #     kakao_email = kakao_account.extra_data.get('email')
    
    # return render(request, 'mypage-1.html', {'reservations': reservations, 'is_kakao_user': is_kakao_user, 'kakao_email': kakao_email})
    return render(request, 'mypage-1.html', {'reservations': reservations,'current_date': current_date})

class UserProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user_profile, created = UserProfile.objects.get_or_create(
            user=request.user)
        initial_data = {
            'username': request.user.username,
            'password': '',  # 빈 문자열로 초기화하여 필드가 비어있는 상태로 표시
            'name': user_profile.name,
            'birthdate': user_profile.birthdate,
            'phonenumber': user_profile.phonenumber,
        }
        form = UserProfileForm(initial=initial_data, instance=user_profile)
        # 사용자가 Kakao 로그인으로 로그인했는지 확인
        try:
            social_account = SocialAccount.objects.get(
                user=request.user, provider='kakao')
            is_kakao_user = True
        except SocialAccount.DoesNotExist:
            is_kakao_user = False

        # 카카오 로그인 사용자인 경우 접근을 막고 메시지 표시
        if is_kakao_user:
            messages.warning(request, '이메일 로그인을 한 회원만 이용 가능합니다.')
            return redirect('mypage:mypage_1')
        return render(request, 'mypage-2.html', {'form': form, 'username': request.user.username, 'user_profile': user_profile})

    def post(self, request):
        user_profile, created = UserProfile.objects.get_or_create(
            user=request.user)
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            user = request.user
            password = request.POST.get('password')
            # print("변경할 비밀번호:", password)  # 비밀번호 변경 시도 시 출력
            if password:
                # print("변경할 비밀번호:", password)  # 비밀번호 변경 시도 시 출력
                user.set_password(password)
                user.save()
            form.save()
            messages.success(request, '정보수정이 완료되었습니다.')
            return redirect('mypage:mypage_2')
        else:
            messages.error(request, '유효하지 않은 값이 있습니다.')
        return render(request, 'mypage-2.html', {'form': form, 'username': request.user.username, 'user_profile': user_profile})

