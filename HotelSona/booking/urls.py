from django.urls import path, include
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us/', views.about_us, name='about_us'),
    path('rooms/', views.rooms, name='rooms'),
    path('booking/', views.booking, name='booking'),
    path('booking-2/', views.booking_2, name='booking_2'),
    path('booking-3/', views.booking_3, name='booking_3'),
    path('booking-3/', views.booking_3, name='booking_3'),
    path('booking-3/complete/', views.booking_3_complete, name='booking_3_complete'),
    path('reservation/delete/<int:pk>/', views.reservation_delete, name='reservation_delete'),

]
