from django.contrib.auth.models import User
from rest_framework import serializers

from .models import ExerciseSession

class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='exercise-user-detail')

    class Meta:
        model = User
        fields = ('url', 'username', 'password', 'email', 'exercise_sessions')
        read_only_fields = ('exercise_sessions',)
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'write_only': True},
        }

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        if validated_data.get('password'):
            instance.set_password(validated_data['password'])
        instance.save()
        return instance

class ExerciseSessionSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        default=serializers.CurrentUserDefault(),
        read_only=True,
        view_name='exercise-user-detail'
    )

    class Meta:
        model = ExerciseSession
        fields = ('url', 'description', 'duration', 'date', 'user')
        read_only_fields = ('user',)
