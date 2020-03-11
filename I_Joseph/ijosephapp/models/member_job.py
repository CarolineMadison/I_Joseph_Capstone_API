from django.db import models
from .member import Member
from .job import Job

class MemberJob(models.Model):
   
    member = models.ForeignKey("Member", on_delete=models.DO_NOTHING)
    job = models.ForeignKey("Job", on_delete=models.CASCADE)

    class Meta:
        ordering = ("product",)