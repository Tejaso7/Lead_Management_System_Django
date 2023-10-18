from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    user_type = models.CharField(max_length=100, default='Admin')


class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)                                                                                        
    contact = models.BigIntegerField()
    college = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    grad_year = models.IntegerField()
    follow_up1 = models.DateField(null=True)
    follow_up2 = models.DateField(null=True)
    follow_up3 = models.DateField(null=True)
    comments = models.CharField(max_length=200, null=True)


class Assignee(models.Model):
    stud_id = models.ForeignKey('lead.Student', on_delete=models.SET_NULL, null=True)
    trainer = models.ForeignKey('lead.User', on_delete=models.SET_NULL, null=True)

                                                                       