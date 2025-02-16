from django.db import models
from rest_api.user_profile.models import UserProfile

class Like(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    likes = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'likes']
        ordering = ['-created_at']