from django.db import models

class Schedule(models.Model):
    content = models.TextField()
    create_date = models.DateTimeField()