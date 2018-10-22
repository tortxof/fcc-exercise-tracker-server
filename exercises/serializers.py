from django.contrib.auth.models import User
from rest_framework import serializers

from .models import ExerciseSession

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'exercise_sessions')
        read_only_fields = ('exercise_sessions',)

class ExerciseSessionSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        default=serializers.CurrentUserDefault(),
        read_only=True,
        view_name='user-detail'
    )

    class Meta:
        model = ExerciseSession
        fields = ('url', 'description', 'duration', 'date', 'user')
        read_only_fields = ('user',)
