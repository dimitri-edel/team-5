from django.db import models


# Create your models here.
class Message(models.Model):
    room_name = models.CharField(max_length=50)
    sender = models.CharField(max_length=50)
    datetime = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=250)


class Connection(models.Model):
    channel = models.CharField(max_length=100, unique=True)
    room = models.CharField(max_length=50)
    connected = models.BooleanField(default=True)
    last_activity = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.room} - {self.channel}"