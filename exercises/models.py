from django.db import models

class ExerciseSession(models.Model):
    description = models.CharField(max_length=255)
    duration = models.IntegerField()
    date = models.DateField(auto_now_add=True)
