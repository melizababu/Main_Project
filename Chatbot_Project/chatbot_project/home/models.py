from django.db import models

# Create your models here.
class Student(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    uni_rollno=models.CharField(max_length=10)
    stream=models.CharField(max_length=10)
    course=models.CharField(max_length=10)
    semester=models.CharField(max_length=10)

    class Meta:
        db_table='Student'