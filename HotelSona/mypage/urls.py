from django.urls import path
from . import views

app_name = 'mypage'

urlpatterns = [
    path('mypage-1/', views.mypage_1, name='mypage_1'),
    path('mypage-2/', views.mypage_2, name='mypage_2'),
]
