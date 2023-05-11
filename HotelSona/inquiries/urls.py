from django.urls import path
from . import views

app_name = 'inquiries'

urlpatterns = [
    
    path('customer-voice/', views.customer_voice, name='customer_voice'),
     path('customer-question/', views.customer_question, name='customer_question'),
     path('customer-detail/<int:question_id>/', views.customer_detail, name='customer_detail'),
   
]
