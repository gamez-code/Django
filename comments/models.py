from django.db import models
from django.conf import settings
# Create your models here.
class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    product = models.ForeignKey(
        'devices.Product',
        related_name='comments',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.content[:20]
