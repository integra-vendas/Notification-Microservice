from django.db import models

class BasicNotifications(models.Model):
    token = models.CharField(max_length=50)
    title = models.CharField(max_length=20)
    message = models.CharField(max_length=50)
