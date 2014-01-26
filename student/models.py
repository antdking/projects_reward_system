from django.db import models


class Student(models.Model):
    user_id = models.IntegerField(unique=True, max_length=5)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    year_group = models.SmallIntegerField(max_length=2)
    tutor_group = models.CharField(max_length=5)