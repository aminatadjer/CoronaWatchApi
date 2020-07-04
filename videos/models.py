from django.db import models
from customauth.models import User

# Create your models here.


class VideoInternaut(models.Model):
    owner = models.ForeignKey(User, related_name='video', on_delete=models.CASCADE, default=1)
    valide = models.BooleanField(default=False)
    supprime = models.BooleanField(default=False)
    vu = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
<<<<<<< HEAD
    commentaire = models.CharField(max_length=20)
    media = models.FileField(null=True, default=None)
=======
    titre = models.CharField(max_length=20)
    video = models.FileField()
>>>>>>> 9bbf2430d2cd45d2668bd465b30cd8cf8a85cd39
