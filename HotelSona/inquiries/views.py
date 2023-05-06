from django.shortcuts import render

# Create your views here.


def customer_voice(request):
    return render(request, 'customer-voice.html')
