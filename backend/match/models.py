from django.db import models
from user_profile.models import UserProfile

class Match(models.Model):
    user1 = models.ForeignKey(UserProfile, related_name='match_user1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(UserProfile, related_name='match_user2', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user1', 'user2']
        ordering = ['-created_at']
