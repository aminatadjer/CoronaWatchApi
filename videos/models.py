from django.db import models

# Create your models here.


class VideoInternaut(models.Model):
    valide = models.BooleanField(default=False)
    supprime = models.BooleanField(default=False)
    vu = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    commentaire = models.CharField(max_length=20)
    media = models.FileField(null=True, default=None)
