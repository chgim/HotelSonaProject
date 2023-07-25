from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register_view, name='register_view'),
    path('logout/', views.logout, name='logout'),  # 추가: logout URL 패턴
    # 카카오 로그인 뷰
    # path('accounts/kakao/login/', views.kakao_login_view, name='kakao_login_view'),
    # # 카카오 로그인 콜백 URL, 이후 구현에 따라 추가
    # path('accounts/kakao/login/callback/',
    #      views.kakao_login_callback_view, name='kakao_login_callback_view'),
]
