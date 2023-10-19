from django.db import models

# Create your models here.
class student(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    current_class = models.CharField(max_length=50)
    age = models.IntegerField()
    