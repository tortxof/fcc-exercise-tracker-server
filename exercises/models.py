from datetime import date

from django.db import models

class ExerciseSession(models.Model):
    description = models.CharField(max_length=255)
    duration = models.PositiveIntegerField('Duration minutes')
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.description
