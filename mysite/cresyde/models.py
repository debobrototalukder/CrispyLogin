from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import CharField, IntegerField


class Profile(models.Model):
    country = CharField(max_length=200)
    pNumber = IntegerField()