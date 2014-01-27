from django.db.models import Max

from student.models import Student, Points


def create_student_object(first_name, last_name, year_group, tutor_group):
    """
    function for creating a student object, that will be returned
    input:
      first_name: The first name of the student
      last_name: The last name of the student
      year_group: The year group the student is in
      tutor_group: The tutor group the student is in
    output:
      student: A user object containing:
        user_id: unique identifier for the student object
        first_name: of the teacher
        last_name: of the teacher
        year_group: of the student
        tutor_group: of the student
    """
    last_id = Student.objects.aggregate(Max('user_id')).get('user_id__max', None)
    if not last_id:
        user_id = 1
    else:
        user_id = int(last_id) + 1
    student = Student(
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
        year_group=year_group,
        tutor_group=tutor_group)
    return student

def assign_student_point(user_id, points, added, reason):
    student = Student.objects.get(user_id=user_id)
    point = Points(
        student=student,
        points=points,
        added=added,
        reason=reason
    )
    return point