from django.db import models
from django.db import models
from customauth.models import User

# Create your models here.


class EtatSante(models.Model):
    owner = models.ForeignKey(
        User, related_name='etatSante', on_delete=models.CASCADE, default=1)
    date = models.DateTimeField()
    poids = models.CharField(max_length=20)
    temperature = models.CharField(max_length=20)
    rythmeCardiaque = models.CharField(max_length=20)
    media = models.FileField(null=True, default=None)
