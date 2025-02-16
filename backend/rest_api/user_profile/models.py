from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('P', 'Prefer not to say'),
    ]

    profile_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    display_name = models.CharField(max_length=100)
    age = models.IntegerField()
    is_online = models.BooleanField(default=False)
    bio = models.TextField(blank=True)
    avatar_url = models.URLField(blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    sexual_orientation = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    contact = models.CharField(max_length=100, blank=True)
    interests = models.CharField(max_length=255, blank=True)
    other_details = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_profile'
        verbose_name = _('User Profile')
        verbose_name_plural = _('User Profiles')

    def __str__(self):
        return f"{self.display_name} - {self.user.username}" 