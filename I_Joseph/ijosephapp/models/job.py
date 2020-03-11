from django.db import models
from .member import Member
from .job_category import JobCategory

class Job(models.Model):

    title = models.CharField(max_length=50)
    category = models.ForeignKey("JobCategory", on_delete=models.DO_NOTHING)
    location = models.CharField(max_length=255)
    description = models.IntegerField()
    isActive = models.BooleanField()
    isCompleted = models.BooleanField()
    createdAt = models.DateTimeField(auto_now_add=True)
    member = models.ForeignKey("Member", on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ("title",)
