from django.db import models

# Create your models here.
class StudentData(models.Model):
    name=models.TextField(max_length=100)
    collegename=models.TextField(max_length=100)
    marks=models.IntegerField()
    result=models.TextField(max_length=10)
    loc=models.TextField(max_length=50)

    def __str__(self):
        return self.name