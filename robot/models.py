from django.db import models

# Create your models here.


class Veille(models.Model):
    TYPE = (
        ('youtube', 'scrapped from youtube'),
        ('twitter', 'scrapped from twitter'),
        ('google', 'scrapped from google search feed'),
    )
    url = models.URLField()
    type=models.CharField(
        max_length=50,
        choices=TYPE,
        default='youtube'
    )
    titre = models.TextField()
    description = models.TextField()
    date= models.CharField(max_length=40, default=None)

    valide = models.BooleanField(default=False)
    supprime = models.BooleanField(default=False)


    def __str__(self):
        return "%s, %s" % (self.titre, self.description)
