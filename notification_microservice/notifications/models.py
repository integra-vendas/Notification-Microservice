from django.db import models

class ProfileToken(models.Model):
    user_id = models.IntegerField(default=0)
    user_token = models.CharField(max_length=50)
