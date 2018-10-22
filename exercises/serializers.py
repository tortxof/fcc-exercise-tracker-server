from django.contrib.auth.models import User
from rest_framework import serializers

from .models import ExerciseSession

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'exercise_sessions')

class ExerciseSessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExerciseSession
        fields = ('url', 'description', 'duration', 'date', 'user')