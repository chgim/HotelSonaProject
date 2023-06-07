from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='UploadAdminImages/') # ImageField Pillow 라이브러리 설치 필요
    price = models.PositiveIntegerField()
    size = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()


    def __str__(self):
        return self.name

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guest_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=16)  # xxxx xxxx xxxx xxxx
    expiry_date = models.CharField(max_length=5)  # mm/yy: 5개