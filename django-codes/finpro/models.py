from django.db import models
from django.utils import timezone

class Text(models.Model):
    text = models.TextField(null=False, blank=False)
    created_date = models.DateTimeField(default=timezone.now)
    result = models.CharField(max_length=20, null=True, blank=True)
