from django.urls import path
from mypage.views import mypage_1, UserProfileView

app_name = 'mypage'

urlpatterns = [
    path('mypage-1/', mypage_1, name='mypage_1'),
    path('mypage-2/', UserProfileView.as_view(), name='mypage_2'),
]
