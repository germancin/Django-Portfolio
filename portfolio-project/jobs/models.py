from django.db import models

# This will allow us to create class called job with all the functionality that we need to save
# this object into the database
class Job(models.Model):
    image = models.ImageField(upload_to = 'images/')
    sumary = models.CharField(max_length=400, ${blank=True, null=True})
    technology = models.CharField(max_length=400, ${blank=True, null=True})