from django.contrib.auth import get_user_model
from django.db import models

from customauth.models import User
from report.models import Region




class EtatSante(models.Model):
    poids = models.FloatField()
    temperature = models.FloatField()
    rythmeCardiaque = models.FloatField()
    suspect = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s (Kg), %s (C), %s" % (self.poids, self.temperature, self.rythmeCardiaque, self.suspect)

# utilisateur web






class Publication(models.Model):
    valide = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)


class VideoInternaut(Publication):
    contenu = models.OneToOneField(
        Publication, on_delete=models.CASCADE, parent_link=True)
    titre = models.CharField(max_length=20)
    description = models.TextField()
    video = models.FileField()


class InformationsVirus(Publication):
    contenu = models.OneToOneField(
        Publication, on_delete=models.CASCADE, parent_link=True)
    region = models.OneToOneField(Region, on_delete=models.CASCADE)



class RebotSource(Publication):
    contenu = models.OneToOneField(
        Publication, on_delete=models.CASCADE, parent_link=True)
    source = models.TextField(max_length=20)
    lien = models.URLField()


class Comment(models.Model):

    content = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)

    def __str__(self):
        return "%s, %s" % (self.content, self.comment_date)

    class Meta:
        ordering = ['comment_date']

    @property
    def owner(self):
        return self.user


class Notification(models.Model):
    content = models.TextField()
