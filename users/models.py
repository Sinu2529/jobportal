from django.db import models
class jobs(models.Model):
    title=models.CharField(max_length=50)
    desp=models.TextField()
    job_type=models.CharField(max_length=10)
    stipend=models.IntegerField()


