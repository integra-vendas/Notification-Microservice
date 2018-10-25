from django.shortcuts import render
from .serializers import BasicNotificationsSerializer
from notifications.models import BasicNotifications
from rest_framework.viewsets import ModelViewSet

class BasicNotificationsViewSet(ModelViewSet):
    queryset = BasicNotifications.objects.all()
    serializer_class = BasicNotificationsSerializer

    def get_queryset(self):
        token = self.request.query_params.get("token")
        return BasicNotifications.objects.filter(token=token)
