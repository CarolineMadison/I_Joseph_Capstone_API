from django.contrib.auth.models import User
from django.db import models
from .job import Job

class UserJob(models.Model):
   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job = models.ForeignKey("Job", on_delete=models.CASCADE)

    class Meta:
        ordering = ("job",)