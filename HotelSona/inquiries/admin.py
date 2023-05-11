from django.contrib import admin
from .models import Question, Answer

class AnswerAdmin(admin.ModelAdmin):
    model = Answer
    fields = ['content'] # 수정 가능한 필드 지정

admin.site.register(Question)

admin.site.register(Answer, AnswerAdmin)
