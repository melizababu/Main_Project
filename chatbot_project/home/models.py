# models.py
from django.db import models


class BusDetails(models.Model):
    busid = models.CharField(max_length=10)
    bus_no = models.CharField(max_length=10)
    route_from = models.CharField(max_length=100)
    driver_name = models.CharField(max_length=100)
    staff_incharge = models.CharField(max_length=100)
    driver_phone = models.CharField(max_length=15)
    staff_phone = models.CharField(max_length=15)
    destination = models.CharField(max_length=100)
    fee_to_each_location = models.JSONField()
    distance_to_each_location = models.JSONField()
    time_to_each_destination = models.JSONField()

    def __str__(self):
        return f'Bus {self.busid}'



# Django model for SQL Database (e.g., SQLite, PostgreSQL)

"""
class Student(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    uni_rollno = models.CharField(max_length=10)
    stream = models.CharField(max_length=10)
    course = models.CharField(max_length=10)
    semester = models.CharField(max_length=10)

    class Meta:
        db_table = 'Student'

# Django model for FAQ (SQL)
class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    
    def __str__(self):
        return self.question
"""