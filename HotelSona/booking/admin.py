from django.contrib import admin
from .models import Room

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name','image', 'price', 'size', 'capacity','availRoom')
    # 필요한 경우 다른 필드도 추가할 수 있습니다

admin.site.register(Room, RoomAdmin)
