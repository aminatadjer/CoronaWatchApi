from django.db import models

# Create your models here.


class Region(models.Model):
    nom = models.TextField(max_length=20)
    suspect = models.IntegerField()
    confirme = models.IntegerField()
    critique = models.IntegerField()
    mort = models.IntegerField()
    guerie = models.IntegerField()


class CasSignalee(models.Model):
    valide = models.BooleanField(default=False)
    supprime = models.BooleanField(default=False)
    vu = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, default=2)
    media = models.FileField()
    commentaire = models.TextField(max_length=40)
