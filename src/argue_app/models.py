from django.db import models
import django.utils.timezone as tz
from django.contrib.auth.models import User
import datetime


# class Data(models.Model):
#     date_time = models.DateTimeField(blank=False)
#     type = models.ForeignKey('DataType', blank=False, on_delete=True)
#     value = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True)


class Profile(models.Model):
    bio = models.CharField(max_length=200)
    rank = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # class meta:
    #     abstract = True


class Topic(models.Model):
    topic_name = models.CharField(max_length=50)


class Argument(models.Model):
    last_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=200, default="Ongoing")
    topic_name = models.ForeignKey(Topic, on_delete=models.CASCADE, default="")
    description = models.CharField(max_length=400, default="")


class Lobby(models.Model):
    arguement = models.ForeignKey(Argument, on_delete=models.CASCADE)
    max_participants = models.IntegerField()
    participants = models.ManyToManyField(Profile)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class ChatMessage(models.Model):
    profile = models.CharField(max_length=30)
    timestamp = datetime.datetime.now()
    message = models.CharField(max_length=200)
