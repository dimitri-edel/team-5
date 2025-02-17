from django.db import models

from user_profile.models import UserProfile

class Dislikes(models.Model):
    user = models.ForeignKey(UserProfile, related_name='disliked_profiles', on_delete=models.CASCADE)
    dislikes = models.ForeignKey(UserProfile, related_name='disliked_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'dislikes']
        ordering = ['-created_at']
