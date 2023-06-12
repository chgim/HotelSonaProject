from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room
# Create your views here.


def about_us(request):
    return render(request, 'about-us.html')

@login_required
def booking_2(request):
    if request.method == "POST":
        check_in = request.POST.get("check-in")
        check_out = request.POST.get("check-out")
        guest_count = request.POST.get("guest")

        # 방 예약 가능한 조건을 쿼리로 작성하여 필터링
        available_rooms = Room.objects.filter(capacity__gte=guest_count, availRoom__gt=0) # availRoom이 1보다 작지 않고 guest가 각 룸의 수용인원보다 커야함.

        return render(request, "booking-2.html", {'rooms': available_rooms})

    return render(request, "booking-2.html")

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
