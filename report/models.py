from django.db import models
from map.models import Region
from customauth.models import User

# Create your models here.



class CasSignalee(models.Model):
    owner= models.ForeignKey(User, related_name='cas', on_delete=models.CASCADE, default=1)
    valide = models.BooleanField(default=False)
    supprime = models.BooleanField(default=False)
    vu = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, default=2)
    media = models.FileField(null=True, default=None)
    commentaire = models.TextField(max_length=40)
