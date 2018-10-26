from django.contrib.auth.models import User
from rest_framework import viewsets
from djoser.views import UserViewSet as DjoserUserViewSet

from .models import ExerciseSession
from .serializers import UserSerializer, ExerciseSessionSerializer
from .permissions import UserPermission, ExerciseSessionPermission

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)

class ExerciseSessionViewSet(viewsets.ModelViewSet):
    queryset = ExerciseSession.objects.all()
    serializer_class = ExerciseSessionSerializer
    permission_classes = (ExerciseSessionPermission,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
