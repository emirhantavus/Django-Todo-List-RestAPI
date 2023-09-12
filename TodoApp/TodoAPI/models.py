from django.db import models
from datetime import datetime

class Task(models.Model):
      title = models.CharField(max_length=255)
      description = models.TextField(null=True, blank=True)
      completed = models.BooleanField(default=False)
      created_at = models.DateTimeField(auto_now=True)
      user = models.CharField(max_length=50)

      def __str__(self):
            return self.title