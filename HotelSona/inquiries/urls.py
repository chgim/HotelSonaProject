from django.urls import path
from . import views

app_name = 'inquiries'

urlpatterns = [
    path('customer-voice/', views.customer_voice, name='customer_voice'),
]
