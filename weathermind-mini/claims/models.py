from django.db import models
from django.contrib.auth.models import User

class Claim(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('done', 'Done'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='claims', null=True, blank=True)
    photo = models.ImageField(upload_to='claims/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    result = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        username = self.user.username if self.user else 'Anonymous'
        return f'Claim #{self.id} by {username}'

