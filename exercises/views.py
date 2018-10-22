from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, viewsets, permissions

from .models import ExerciseSession
from .serializers import UserSerializer, ExerciseSessionSerializer
from .permissions import IsOwnerOrReadOnly, IsSelfOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsSelfOrReadOnly,
    )

class ExerciseSessionViewSet(viewsets.ModelViewSet):
    queryset = ExerciseSession.objects.all()
    serializer_class = ExerciseSessionSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )
