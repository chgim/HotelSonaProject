from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Room(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='UploadAdminImages/') # 관리자 페이지에서 업로드 가능
    price = models.PositiveIntegerField()
    size = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    availRoom = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):# Room 객체가 저장될 때 호출
        if self.pk:
            reservations = Reservation.objects.filter(room=self)
            today = timezone.now().date()
            for reservation in reservations:# 예약 정보 중 체크아웃 날짜가 오늘보다 이전인 경우 availRoom을 1 증가
                if reservation.check_out < today:
                    self.availRoom += 1
        super().save(*args, **kwargs) # save 메서드를 실행하여 객체를 저장





class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guest_count = models.IntegerField()
    card_number = models.CharField(max_length=16)
    expiry_date = models.CharField(max_length=5)
    guest_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()

    def __str__(self):
        return f"Reservation for {self.guest_name} - Room {self.room.name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs): # 예약 정보 삭제 시 해당 객실 availRoom +1
        self.room.availRoom += 1
        self.room.save()
        super().delete(*args, **kwargs)