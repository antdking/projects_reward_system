from django.contrib import admin
from student.models import Student, Points


class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['first_name', 'last_name']})
    ]
admin.site.register(Student)
admin.site.register(Points)