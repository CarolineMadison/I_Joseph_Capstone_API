from django.contrib.auth.models import User
from django.db import models
from .job_category import JobCategory

class Job(models.Model):

    title = models.CharField(max_length=50)
    category = models.ForeignKey(JobCategory, on_delete=models.DO_NOTHING)
    location = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    isCompleted = models.BooleanField()
    createdAt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ("title",)