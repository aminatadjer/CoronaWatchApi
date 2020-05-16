from django.db import models

# Create your models here.


class Article(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    valide = models.BooleanField(default=False)
    supprime = models.BooleanField(default=False)
    vu = models.BooleanField(default=False)
    titre = models.CharField(max_length=20)
    contenu = models.TextField()
    media = models.FileField(blank=False, null=False)
