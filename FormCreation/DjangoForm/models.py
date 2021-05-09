from django.db import models

# Create your models here.

from django.db import models

class StudentForm(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()

    class Meta:
        db_table = "student"
