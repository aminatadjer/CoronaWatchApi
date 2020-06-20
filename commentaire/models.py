from django.db import models

# Create your models here.

class Comment(models.Model):
    supprime = models.BooleanField(default=False)
    contenu = models.TextField()
