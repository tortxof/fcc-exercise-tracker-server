from datetime import date

from django.contrib.auth.models import User
from django.db import models

class ExerciseSession(models.Model):
    description = models.CharField(max_length=255)
    duration = models.PositiveIntegerField('Duration minutes')
    date = models.DateField(default=date.today)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='exercise_sessions',
    )

    def __str__(self):
        return self.description
