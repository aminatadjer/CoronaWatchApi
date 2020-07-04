from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from django.contrib.auth.models import (
    AbstractUser
)
# Create your models here.

editorPerm=[('article.add_article', 'article.view_article')]
moderatorPerm=['article.delete_article', 'article.change_article']
healthagentPerm=[]

class User(AbstractUser):
    """customauth/login-related fields"""
    ROLE = (
        ('final user', 'The final user (Android user).'),
        ('health agent', 'The health agent.'),
        ('moderator', 'The Moderator.'),
        ('editor', 'The editor of articles'),
    )
    role = models.CharField(
        max_length=32,
        choices=ROLE,
        default='final user'
    )
    REQUIRED_FIELDS = ['role']

    def __str__(self):
        return super().__str__()


@receiver(post_save, sender=User)
def define_permission(sender, **kwargs):
    if User.objects.last().role == 'editor':
        print("editor saved")

    elif User.objects.last().role == 'moderator':
        print("moderator saved")
    elif User.objects.last().role == 'health agent':
        print("health agent saved")
    elif User.objects.last().role == 'final user':
        print("final user saved")
    else:
        print("error in role model")