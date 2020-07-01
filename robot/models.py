from django.db import models

# Create your models here.


class VideoYoutube(models.Model):
    valide = models.BooleanField(default=False)
    supprime = models.BooleanField(default=False)
    titre = models.TextField()
    description = models.TextField()
    url = models.URLField(primary_key=True)


class Tweets(models.Model):
    proprio = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    date = models.CharField(max_length=50)
    valide = models.BooleanField(default=False)
    supprime = models.BooleanField(default=False)


class GoogleSearchResult(models.Model):
    valide = models.BooleanField(default=False)
    supprime = models.BooleanField(default=False)
    titre = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    date = models.CharField(max_length=50)

    class Meta:
        unique_together = ["url"]

    def __str__(self):
        return "%s, %s" % (self.titre, self.description)
