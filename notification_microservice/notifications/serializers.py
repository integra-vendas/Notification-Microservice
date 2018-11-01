from rest_framework import serializers
from .models import ProfileToken

class ProfileTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileToken
        fields = '__all__'
