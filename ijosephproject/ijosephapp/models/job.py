from django.contrib.auth.models import User
from django.db import models
from .job_category import JobCategory

class Job(models.Model):

    title = models.CharField(max_length=50)
    category = models.ForeignKey("JobCategory", on_delete=models.DO_NOTHING)
    location = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    isActive = models.BooleanField()
    isCompleted = models.BooleanField()
    createdAt = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ("title",)