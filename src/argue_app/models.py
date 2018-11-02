from django.db import models
import django.utils.timezone as tz
from django.contrib.auth.models import User
import datetime


class Profile(models.Model):
    bio = models.CharField(max_length=200)
    rank = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Topic(models.Model):
    topic_name = models.CharField(max_length=50)


class Status(models.Model):
    status_name = models.CharField(max_length=50)


class ChatLobby(models.Model):
    lobby_name = models.CharField(max_length=50)


class ChatMessage(models.Model):
    writer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateField(null=True, blank=True)
    message = models.CharField(max_length=200)
    chat_lobby = models.ForeignKey(ChatLobby, on_delete=models.CASCADE)


class Argument(models.Model):
    argument_name = models.CharField(max_length=200, default='')
    last_updated = models.DateField(null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    description = models.CharField(max_length=400, default="")
    max_participants = models.IntegerField()
    participants = models.ManyToManyField(Profile)
    creator = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name="creator")
    chat_lobby = models.ForeignKey(ChatLobby, on_delete=models.PROTECT)



