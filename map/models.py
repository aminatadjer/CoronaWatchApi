from django.db import models

# Create your models here.


class Region(models.Model):
    nom = models.TextField(max_length=20)
    longitude = models.FloatField(default=0)
    latitude = models.FloatField(default=0)


class InfoRegion(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, default=2)
    suspect = models.IntegerField()
    confirme = models.IntegerField()
    critique = models.IntegerField()
    mort = models.IntegerField()
    guerie = models.IntegerField()
    degre = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    valide = models.BooleanField(default=False)
    supprime = models.BooleanField(default=False)
    vu = models.BooleanField(default=False)
