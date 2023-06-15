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
        # 필터링 된 룸과 사용자가 이전에 입력했던 form 요소들 return. 
        return render(request, "booking-2.html", {'rooms': available_rooms, 'check_in': check_in, 'check_out': check_out, 'guest_count': guest_count})

    return render(request, "booking-2.html")

@login_required
def booking_3(request):
    check_in = request.GET.get("check-in")
    check_out = request.GET.get("check-out")
    guest_count = request.GET.get("guest")
    selected_room = request.GET.get("selected_room")

    return render(request, 'booking-3.html', {'check_in': check_in, 'check_out': check_out, 'guest_count': guest_count, 'selected_room': selected_room})

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
