from django.db import models


class Student(models.Model):
    user_id = models.IntegerField(unique=True, max_length=5)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    year_group = models.SmallIntegerField(max_length=2)
    tutor_group = models.CharField(max_length=5)

    def points_total(self):
        points_added = Points.objects.filter(student=self)
        points_total = 0
        for point in points_added:
            if point.added:
                points_total += point.points
            else:
                points_total -= point.points
        return int(points_total)

    def __unicode__(self):
        return " ".join([self.first_name, self.last_name])


class Points(models.Model):
    student = models.ForeignKey('Student')
    points = models.PositiveIntegerField(max_length=2)
    added = models.BooleanField(default=True)
    reason = models.CharField(max_length=100)
