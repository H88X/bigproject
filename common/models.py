from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    MEMBERSHIP_CHOICES = [
        ('advertiser', '광고주'),
        ('agency', '광고대행사'),
    ]

    membership_type = models.CharField(max_length=20, choices=MEMBERSHIP_CHOICES)
    phone = models.CharField(max_length=20)
