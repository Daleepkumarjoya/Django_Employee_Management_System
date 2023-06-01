from django.db import models


# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    EmployeeId = models.CharField(max_length=200)
    PhoneNumber = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    working = models.BooleanField(default=False)
    department = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class aboutModel(models.Model):
    AboutEMS = models.TextField()
    SourceName1 = models.CharField(max_length=100)
    SourceAbout1 = models.TextField()
    SourceName2 = models.CharField(max_length=100)
    SourceAbout2 = models.TextField()
    SourceName3 = models.CharField(max_length=100)
    SourceAbout3 = models.TextField()

    def __str__(self):
        return self.AboutEMS
