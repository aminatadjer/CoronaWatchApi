from django.db import models
from customauth.models import User

# Create your models here.

class VideoInternaut(models.Model):
    owner = models.ForeignKey(User, related_name='video', on_delete=models.CASCADE, default=1)
    valide = models.BooleanField(default=False)
    supprime = models.BooleanField(default=False)
    vu = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    titre = models.CharField(max_length=20)
    video = models.FileField()