from django.db import models

class JobCategory(models.Model):

    category = models.CharField(max_length=55)
    
    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ("category",)