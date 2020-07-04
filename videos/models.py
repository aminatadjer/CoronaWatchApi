from django.db import models
from customauth.models import User

# Create your models here.


class VideoInternaut(models.Model):
    owner = models.ForeignKey(
        User, related_name='video', on_delete=models.CASCADE, default=1)
    valide = models.BooleanField(default=False)
    supprime = models.BooleanField(default=False)
    vu = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    commentaire = models.CharField(max_length=20)
    media = models.FileField(null=True, default=None)
