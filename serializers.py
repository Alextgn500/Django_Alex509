# note/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Note

# Сериализатор для модели User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# Сериализатор для модели Note
class NoteSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Note
        fields = ['id', 'title', 'owner']
