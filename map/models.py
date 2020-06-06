from django.db import models
from customauth.models import User
# Create your models here.


class Region(models.Model):
    nom = models.TextField(max_length=20)
    lat = models.FloatField(default=0)
    lang = models.FloatField(default=0)
    ArabicName = models.TextField(max_length=100)
    suspect = models.IntegerField(default=0)
    confirme = models.IntegerField(default=0)
    critique = models.IntegerField(default=0)
    mort = models.IntegerField(default=0)
    guerie = models.IntegerField(default=0)
    degre = models.IntegerField(default=0)
    date_validation = models.DateTimeField()


class HistoriqueRegion(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, default=1)
    suspect = models.IntegerField(default=0)
    confirme = models.IntegerField(default=0)
    critique = models.IntegerField(default=0)
    mort = models.IntegerField(default=0)
    guerie = models.IntegerField(default=0)
    degre = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    agent = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    valide = models.BooleanField(default=False)
    supprime = models.BooleanField(default=False)
    vu = models.BooleanField(default=False)


class CentreReception(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, default=1)
    nom = models.TextField(max_length=50)
    numero = models.TextField(max_length=20)
    adresse = models.TextField(max_length=20)
