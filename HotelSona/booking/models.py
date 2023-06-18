from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Room(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='UploadAdminImages/') # 관리자 페이지에서 업로드 가능
    price = models.PositiveIntegerField()
    size = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 





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
    

    def __str__(self):
        return f"Reservation for {self.guest_name} - Room {self.room.name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        


    def delete(self, *args, **kwargs): 
        super().delete(*args, **kwargs)
        
        