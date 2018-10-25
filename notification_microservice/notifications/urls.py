from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers
from .views import BasicNotificationsViewSet


router = routers.SimpleRouter()
router.register(r'basic_notifications', BasicNotificationsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
