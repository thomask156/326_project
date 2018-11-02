from django.core.management.base import BaseCommand, CommandError
from argue_app.models import *
from django.contrib.auth.models import User
import django.utils.timezone as tz

import logging
from django.utils import timezone

log = logging.getLogger('argue')


class Command(BaseCommand):
    help = 'Configures models for the argue application.'

    def handle(self, *args, **options):
        """Adds default entries for the argue app.
            :returns: None
            """

        user1, created = User.objects.update_or_create(id=1,
                                                       defaults={"username": 'John',
                                                                 "email": 'lennon@thebeatles.com',
                                                                 "password": 'password12345'})
        user1.last_name = 'Lennon'
        user1.save()
        person1, created = Profile.objects.update_or_create(id=1,
                                                            defaults={"bio": "I love dogs. Fight me about it.",
                                                                      "rank": 15,
                                                                      "user": user1})

        user2, created = User.objects.update_or_create(id=2,
                                                       defaults={"username": 'Ringo',
                                                                 "email": 'ringo@thebeatles.com',
                                                                 "password": 'password12345'})
        user2.last_name = 'Star'
        user2.save()
        person2, created = Profile.objects.update_or_create(id=2,
                                                            defaults={"bio": "I eat ice cream in the nude.",
                                                                      "rank": 7,
                                                                      "user": user2})

        user3, created = User.objects.update_or_create(id=3,
                                                       defaults={"username": 'George',
                                                                 "email": 'harrison@thebeatles.com',
                                                                 "password": 'password12345'})
        user3.last_name = 'Harrison'
        user3.save()
        person3, created = Profile.objects.update_or_create(id=3,
                                                            defaults={"bio": "I love dogs. Fight me about it.",
                                                                      "rank": 8,
                                                                      "user": user3})

        topic1, created = Topic.objects.update_or_create(id=1, defaults={"topic_name": "Penguins Vs. Puffins"})
        topic2, created = Topic.objects.update_or_create(id=2, defaults={"topic_name": "Hats Vs. Cats"})
        topic3, created = Topic.objects.update_or_create(id=3, defaults={"topic_name": "Is a hotdog a sandwich"})

        status1, created = Status.objects.update_or_create(id=1, defaults={"status_name": "Not started"})
        status2, created = Status.objects.update_or_create(id=2, defaults={"status_name": "Ongoing"})
        status3, created = Status.objects.update_or_create(id=3, defaults={"status_name": "Cancelled"})
        status4, created = Status.objects.update_or_create(id=4, defaults={"status_name": "Resolved"})
        status5, created = Status.objects.update_or_create(id=5, defaults={"status_name": "Unresolved"})

        global_lobby, created = ChatLobby.objects.update_or_create(id=1, defaults={"lobby_name": "Global lobby"})
        chat_lobby1, created = ChatLobby.objects.update_or_create(id=2, defaults={"lobby_name": "argument 1"})
        chat_lobby2, created = ChatLobby.objects.update_or_create(id=3, defaults={"lobby_name": "argument 2"})
        chat_lobby3, created = ChatLobby.objects.update_or_create(id=4, defaults={"lobby_name": "argument 3"})

        argument1, created = Argument.objects.update_or_create(id=1,
                                                               defaults={"argument_name": "Cats suck",
                                                                         "last_updated": tz.datetime.now(),
                                                                         "status": status4,
                                                                         "topic": topic2,
                                                                         "description": "Cats are like, literally, the worst. I'd take a hat as a pet any day",
                                                                         "max_participants": 3,
                                                                         "creator": person3,
                                                                         "chat_lobby": chat_lobby1})
        argument1.participants.set([person1, person3])
        argument1.save()

        argument2, created = Argument.objects.update_or_create(id=2,
                                                               defaults={"argument_name": "Penguins don't have souls",
                                                                         "last_updated": tz.datetime.now(),
                                                                         "status": status1,
                                                                         "topic": topic1,
                                                                         "description": "Have you even seen penguins? They look like walking toasters. Totally lame.",
                                                                         "max_participants": 2,
                                                                         "creator": person1,
                                                                         "chat_lobby": chat_lobby2})
        argument2.participants.set([person1])
        argument2.save()

        argument3, created = Argument.objects.update_or_create(id=3,
                                                               defaults={"argument_name": "If a hotdog isn't a sandwhich, I'm going to kill myself",
                                                                         "last_updated": tz.datetime.now(),
                                                                         "status": status4,
                                                                         "topic": topic3,
                                                                         "description": "I'm a grown man! I don't want to have to tell my children I'm eating a wiener!",
                                                                         "max_participants": 5,
                                                                         "creator": person1,
                                                                         "chat_lobby": chat_lobby3})
        argument3.participants.set([person1, person2, person3])
        argument3.save()

        message1, created = ChatMessage.objects.update_or_create(id=1,
                                                                 defaults={
                                                                     "writer": person2,
                                                                     "timestamp": tz.datetime.now(),
                                                                     "message": "Yo any of you know any good jams?",
                                                                     "chat_lobby": global_lobby})
        message2, created = ChatMessage.objects.update_or_create(id=2,
                                                                 defaults={
                                                                     "writer": person1,
                                                                     "timestamp": tz.datetime.now(),
                                                                     "message": "I heard 'Come Together' is pretty good",
                                                                     "chat_lobby": global_lobby})
        message3, created = ChatMessage.objects.update_or_create(id=3,
                                                                 defaults={
                                                                     "writer": person3,
                                                                     "timestamp": tz.datetime.now(),
                                                                     "message": "Shut up you wanker",
                                                                     "chat_lobby": global_lobby})

        log.info("Configuration complete")
