from rest_framework import viewsets

from .models import ExerciseSession
from .serializers import ExerciseSessionSerializer
from .permissions import ExerciseSessionPermission

class ExerciseSessionViewSet(viewsets.ModelViewSet):
    queryset = ExerciseSession.objects.all()
    serializer_class = ExerciseSessionSerializer
    permission_classes = (ExerciseSessionPermission,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
