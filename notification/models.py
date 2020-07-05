from django.db import models

# Create your models here.


class Notification(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    titre = models.TextField()
    description = models.TextField()
    typeNotif = models.IntegerField()
    vu = models.BooleanField(default=False)
