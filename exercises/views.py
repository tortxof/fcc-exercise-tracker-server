from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets

from .models import ExerciseSession
from .serializers import UserSerializer, ExerciseSessionSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class ExerciseSessionViewSet(viewsets.ModelViewSet):
    queryset = ExerciseSession.objects.all()
    serializer_class = ExerciseSessionSerializer
