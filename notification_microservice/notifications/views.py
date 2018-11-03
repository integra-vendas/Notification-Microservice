from exponent_server_sdk import PushClient
from exponent_server_sdk import PushMessage
from exponent_server_sdk import PushServerError
from exponent_server_sdk import PushResponseError
from exponent_server_sdk import DeviceNotRegisteredError
from exponent_server_sdk import MessageTooBigError
from exponent_server_sdk import MessageRateExceededError
from requests.exceptions import ConnectionError
from requests.exceptions import HTTPError
from django.shortcuts import render
from .serializers import ProfileTokenSerializer
from notifications.models import ProfileToken
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.conf import settings
import requests
from rest_framework import generics
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_413_REQUEST_ENTITY_TOO_LARGE,
    HTTP_502_BAD_GATEWAY,
    HTTP_503_SERVICE_UNAVAILABLE
)

class UserList(generics.ListCreateAPIView):
    queryset = ProfileToken.objects.all()
    serializer_class = ProfileTokenSerializer

@permission_classes((AllowAny, ))
@api_view(["POST"])
def save_user_token(request):
    user_id = request.data.get('user_id')
    user_token = request.data.get('user_token')

    if (user_id == None or user_token == None):
        return Response({'error':'Usuário não identificado.'}, status=HTTP_400_BAD_REQUEST)

    try:
        user = ProfileToken.objects.get(user_id = user_id)
        user.user_token = user_token
        user.save()
    except:
        ProfileToken.objects.create(
            user_id = user_id,
            user_token = user_token
        )

    return Response(status=HTTP_200_OK)

@api_view(["POST"])
@permission_classes((AllowAny, ))
def send_push_message(request):
    user_id = request.data.get('user_id')
    user_profile = ProfileToken.objects.get(user_id = user_id)
    user_token = user_profile.user_token
    title = request.data['title']
    message = request.data['message']

    try:
        response = PushClient().publish(
            PushMessage(to=user_token, title=title, body=message))
    except:
        return Response({'error':'Não foi possível enviar notificação ao vendedor.'}, status=HTTP_404_NOT_FOUND)
    try:
        response.validate_response()
    except:
        return Response({'error':'Não foi possível validar o token de notificação.'}, status=HTTP_400_BAD_REQUEST)

    return Response(status=HTTP_200_OK)
