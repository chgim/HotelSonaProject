from django.contrib.auth.decorators import login_required
from booking.models import Reservation

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from accounts.forms import UserProfileForm
from accounts.models import UserProfile

from django.shortcuts import get_object_or_404

@login_required
def mypage_1(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'mypage-1.html', {'reservations': reservations})



class UserProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        initial_data = {
            'username': request.user.username,
            'password': '',  # 빈 문자열로 초기화하여 필드가 비어있는 상태로 표시
            'name': user_profile.name,
            'birthdate': user_profile.birthdate,
            'phonenumber': user_profile.phonenumber,
        }
        form = UserProfileForm(initial=initial_data, instance=user_profile)
        return render(request, 'mypage-2.html', {'form': form, 'username': request.user.username, 'user_profile': user_profile})

    def post(self, request):
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
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