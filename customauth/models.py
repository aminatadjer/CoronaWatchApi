from django.db import models
from django.contrib.auth.models import (
    AbstractUser
)
# Create your models here.
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