from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import CharField, IntegerField


class Profile(models.Model):
    country = models.CharField(max_length=200, default='empty')
    number = models.IntegerField(default=0)
    fKey = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
