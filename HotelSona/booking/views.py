from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Room
from .models import Reservation
from datetime import timedelta
from django.utils import timezone
from django.contrib import messages
from django.http import HttpResponseNotAllowed
from datetime import datetime
from decimal import Decimal
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
        available_rooms = Room.objects.filter(capacity__gte=guest_count) # guest가 각 룸의 수용인원보다 커야함.
        # 필터링 된 룸과 사용자가 이전에 입력했던 form 요소들 return. 
        return render(request, "booking-2.html", {'rooms': available_rooms, 'check_in': check_in, 'check_out': check_out, 'guest_count': guest_count})

    return render(request, "booking-2.html")

@login_required
def booking_3(request):
    check_in = request.GET.get("check-in")
    check_out = request.GET.get("check-out")
    guest_count = request.GET.get("guest")
    selected_room = request.GET.get("selected_room")

    room = Room.objects.get(name=selected_room)
    room_price = room.price
    # int(체크아웃-체크인)*객실 1박 가격
    # 숙박 기간 계산하기:  
    check_in = datetime.strptime(check_in, "%Y-%m-%d").date()
    check_out = datetime.strptime(check_out, "%Y-%m-%d").date()
    duration = (check_out - check_in).days

    # 예약 가격 계산하기
    total_price = room_price * Decimal(duration)

    return render(request, 'booking-3.html', {'check_in': check_in, 'check_out': check_out, 'guest_count': guest_count, 'selected_room': selected_room, 'total_price':total_price})

 # 실제 예약 시스템


@login_required
def booking_3_complete(request):
    if request.method == "POST":
        check_in = request.POST.get("check_in")
        check_out = request.POST.get("check_out")
        guest_count = request.POST.get("guest_count")
        selected_room = request.POST.get("selected_room")
        total_price = int(request.POST.get("total_price"))
        moveNumber1 = request.POST.get('moveNumber1', '')
        moveNumber2 = request.POST.get('moveNumber2', '')
        moveNumber3 = request.POST.get('moveNumber3', '')
        moveNumber4 = request.POST.get('moveNumber4', '')
        card_number = moveNumber1 + moveNumber2 + moveNumber3 + moveNumber4 # input 필드 네개로 이루어진 카드 번호 합쳐서 보내기
        expiry_date = request.POST.get("validThru")
        guest_name = request.user.username
        
        
        # 문자열을 datetime 객체로 변환
        # check_in = datetime.strptime(check_in, "%Y-%m-%d").date()
        # check_out = datetime.strptime(check_out, "%Y-%m-%d").date()
        check_in = datetime.strptime(check_in, "%Y년 %m월 %d일").date().strftime("%Y-%m-%d")
        check_out = datetime.strptime(check_out, "%Y년 %m월 %d일").date().strftime("%Y-%m-%d")

        room = Room.objects.get(name=selected_room)
        
        # 예약 내역 중 중복 예약 확인
        # 현재 예약 하려는 check_in 날짜가 예약 내역의 check_out 날짜보다 작으면
        existing_reservation = Reservation.objects.filter(user=request.user, guest_name=guest_name,
                                                          check_out__gte=check_in, check_in__lte=check_out)
        if existing_reservation.exists():
            messages.error(request, "이미 예약된 내역이 있습니다.")
            return redirect('booking:booking_3')
        else:
            # reservation 모델에 저장
            reservation = Reservation.objects.create(user=request.user, room=room, check_in=check_in, check_out=check_out,
                                                 guest_count=guest_count, card_number=card_number,
                                                 expiry_date=expiry_date, guest_name=guest_name,total_price=total_price,
                                                 )
            reservation.save()  # Reservation 모델의 save 메서드 호출하여 예약 정보 저장
            # 예약 완료 메시지 표시
            messages.success(request, "예약이 완료되었습니다.")
            return redirect('booking:index')
            
    else:
        return HttpResponseNotAllowed(['POST'])
