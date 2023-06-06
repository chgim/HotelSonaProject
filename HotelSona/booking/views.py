from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


def about_us(request):
    return render(request, 'about-us.html')

@login_required
def booking_2(request):
    return render(request, 'booking-2.html')

@login_required
def booking_3(request):
    return render(request, 'booking-3.html')

@login_required
def booking(request):
    return render(request, 'booking.html')


def index(request):
    return render(request, 'index.html')


def rooms(request):
    return render(request, 'rooms.html')
