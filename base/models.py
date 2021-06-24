from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Text(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True)
    text = models.TextField(null=False, blank=False)
    client = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    #emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.text
