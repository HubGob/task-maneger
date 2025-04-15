from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    # Relationship: Each task belongs to one user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Task attributes
    title = models.CharField(max_length=200)        # Short text
    description = models.TextField(blank=True)      # Long text (optional)
    completed = models.BooleanField(default=False)  # True/False flag
    created = models.DateTimeField(auto_now_add=True) # Auto-set timestamp