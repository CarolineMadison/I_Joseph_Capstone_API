from django.contrib.auth.models import User
from django.db import models
from .job import Job

class UserJob(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    class Meta:
        ordering = ("job",)

        # NEED TO MAKE SURE THAT WHEN I DESELECT A USERJOB IT DELETES IT FROM THIS TABLE WITHOUT DELETING IT FROM JOB TABLE OR DELETING THE USER