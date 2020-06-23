from django.db import models

# Create your models here.

class VideoInternaut(models.Model):
    valide = models.BooleanField(default=False)
    supprime = models.BooleanField(default=False)
    vu = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    titre = models.CharField(max_length=20)
    description = models.TextField()
    video = models.FileField()