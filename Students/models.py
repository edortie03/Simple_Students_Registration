from django.db import models

class Student(models.Model):
    registration_number = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    year_of_study = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.full_name
