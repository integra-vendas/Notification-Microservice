from rest_framework import serializers
from .models import BasicNotifications


class BasicNotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicNotifications
        fields = '__all__'
