from django.contrib import admin
from .models import Room

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name','image', 'price', 'size', 'capacity','availRoom')
    

admin.site.register(Room, RoomAdmin)
