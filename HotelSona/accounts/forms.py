from django import forms
from django.contrib.auth.forms import UserChangeForm

from accounts.models import UserProfile

class UserProfileForm(UserChangeForm):
    password = None  # 비밀번호 필드를 제외합니다.

    class Meta:
        model = UserProfile
        fields = ['name', 'birthdate', 'email', 'phonenumber']