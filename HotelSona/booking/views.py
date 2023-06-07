from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room
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

# 두개는 끝
def index(request):
    all_rooms = Room.objects.all()
    return render(request, 'index.html', {'rooms': all_rooms})


def rooms(request):
    all_rooms = Room.objects.all()
    return render(request, 'rooms.html', {'rooms': all_rooms})
