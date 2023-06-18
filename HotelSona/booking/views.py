from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Room
from .models import Reservation
from datetime import timedelta
from django.utils import timezone
from django.contrib import messages
from django.http import HttpResponseNotAllowed
from datetime import datetime
# Create your views here.


def about_us(request):
    return render(request, 'about-us.html')


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

 # 실제 예약 시스템
 # 예약 생성, 예약된 날짜동안 availRoom -1

@login_required
def booking_3_complete(request):
    if request.method == "POST":
        check_in = request.POST.get("check_in")
        check_out = request.POST.get("check_out")
        guest_count = request.POST.get("guest_count")
        selected_room = request.POST.get("selected_room")
        moveNumber1 = request.POST.get('moveNumber1', '')
        moveNumber2 = request.POST.get('moveNumber2', '')
        moveNumber3 = request.POST.get('moveNumber3', '')
        moveNumber4 = request.POST.get('moveNumber4', '')
        card_number = moveNumber1 + moveNumber2 + moveNumber3 + moveNumber4 # input 필드 네개로 이루어진 카드 번호 합쳐서 보내기
        expiry_date = request.POST.get("validThru")
        guest_name = request.user.username
        email = request.user.email
        
        # 문자열을 datetime 객체로 변환
        check_in = datetime.strptime(check_in, "%Y-%m-%d").date()
        check_out = datetime.strptime(check_out, "%Y-%m-%d").date()

        room = Room.objects.get(name=selected_room)
        
    

        if room.availRoom < 1: # 해당 객실의 사용 가능한 방이 없을 때
            messages.error(request, "선택한 객실은 예약 가능한 객실이 아닙니다.")
            return redirect('booking:booking_2')

        # reservation 모델에 저장
        reservation = Reservation.objects.create(user=request.user, room=room, check_in=check_in, check_out=check_out,
                                                 guest_count=guest_count, card_number=card_number,
                                                 expiry_date=expiry_date, guest_name=guest_name,
                                                 email=email)

        # 선택한 날짜 기간 동안 해당 객실의 availRoom을 -1 감소
        duration = (check_out - check_in).days + 1
        for day in range(duration):
            current_date = check_in + timedelta(days=day)
            if room.availRoom > 0:
                room.availRoom -= 1
            room.save()

        reservation.save()

        # 예약 완료 메시지 표시
        messages.success(request, "예약이 완료되었습니다.")

        return redirect('booking:index')
    else:
        return HttpResponseNotAllowed(['POST'])
