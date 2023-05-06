from django.shortcuts import render

# Create your views here.


def about_us(request):
    return render(request, 'about-us.html')


def booking_2(request):
    return render(request, 'booking-2.html')


def booking_3(request):
    return render(request, 'booking-3.html')


def booking(request):
    return render(request, 'booking.html')


def index(request):
    return render(request, 'index.html')


def rooms(request):
    return render(request, 'rooms.html')
