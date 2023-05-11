from django.db import models
from django.utils import timezone

class Answer(models.Model):
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
   

    def __str__(self):
        return self.content

class Question(models.Model):
    author = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    answer = models.OneToOneField('Answer', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
