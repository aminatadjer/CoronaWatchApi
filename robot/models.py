from django.db import models

# Create your models here.


class VideoYoutube(models.Model):
    valide = models.BooleanField(default=False)
    supprime = models.BooleanField(default=False)
    titre = models.CharField(max_length=1000)
    description = models.TextField()
    url = models.URLField(primary_key=True)


class Tweets(models.Model):
    valide = models.BooleanField(default=False)
    supprime = models.BooleanField(default=False)
    url = models.URLField()


class GoogleSearchResult(models.Model):
    valide = models.BooleanField(default=False)
    supprime = models.BooleanField(default=False)
    titre = models.CharField(max_length=20)
    description = models.TextField()
    url = models.URLField()
    date = models.CharField(max_length=50)

    class Meta:
        unique_together = ["url"]

    def __str__(self):
        return "%s, %s" % (self.titre, self.description)
