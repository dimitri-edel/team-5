from django.db import models
from user_profile.models import UserProfile

class Like(models.Model):
    user = models.ForeignKey(UserProfile, related_name='source_profile', on_delete=models.CASCADE)
    likes = models.ForeignKey(UserProfile, related_name='target_profile', on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'likes']        
        ordering = ['-created_at']