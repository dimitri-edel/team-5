from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profiles")
    display_name = models.CharField(max_length=255)
    age = models.IntegerField()
    is_online = models.BooleanField(default=False)
    bio = models.TextField(blank=True, null=True)
    avatar_url = models.URLField(max_length=500, blank=True, null=True)
    gender = models.CharField(max_length=50, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    sexual_orientation = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    other_details = models.JSONField(default=dict, blank=True, null=True)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.display_name

