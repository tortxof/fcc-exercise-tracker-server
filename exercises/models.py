from django.db import models

class ExerciseSession(models.Model):
    description = models.CharField(max_length=255)
    duration = models.PositiveIntegerField('Duration minutes')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.description
