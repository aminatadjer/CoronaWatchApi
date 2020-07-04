from django.db import models
from customauth.models import User

# Create your models here.


class Article(models.Model):
    owner = models.ForeignKey(User, related_name='article', on_delete=models.CASCADE, default=1)
    url = models.CharField(max_length=200, default="")
    date = models.DateTimeField(auto_now_add=True)
    valide = models.BooleanField(default=False)
    supprime = models.BooleanField(default=False)
    vu = models.BooleanField(default=False)
    titre = models.CharField(max_length=20)
    contenu = models.TextField()
    media = models.FileField(null=True, default=None)
