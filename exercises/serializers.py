from rest_framework import serializers

from .models import ExerciseSession

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
