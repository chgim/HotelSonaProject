from django.contrib import admin
from .models import Room, Reservation


class RoomAdmin(admin.ModelAdmin):
    list_display = ('name','image', 'price', 'size', 'capacity','availRoom')
    
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'email','room', 'check_in', 'check_out', 'guest_count', 'card_number', 'expiry_date', 'guest_name', 'created_at')

admin.site.register(Room, RoomAdmin)
admin.site.register(Reservation, ReservationAdmin)