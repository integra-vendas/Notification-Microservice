from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers
from .views import send_push_message, save_user_token, UserList

urlpatterns = [
    url(r'^user_list/$', UserList.as_view()),
    path('send_push_message/', send_push_message),
    path('save_user_token/', save_user_token)
]
