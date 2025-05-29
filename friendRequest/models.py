from django.db import models
from accounts.models import CustomUser

# Create your models here.

class FriendRequest(models.Model):
    from_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name = 'sent_friend_request')
    to_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name = 'received_friend_request')
    status = models.CharField(max_length=10, choices = [('pending','Pending'),('accepted','Accepted'),('rejected','Rejected',)], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('from_user', 'to_user')

    def __str__(self):
        return f"{self.from_user.username} {self.to_user.username} [{self.status}]"