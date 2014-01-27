from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.shortcuts import redirect, render
from django.template import RequestContext

from student import utils
from student.models import Student


class CreateStudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'year_group', 'tutor_group']


@login_required()
def create_student(request):
    if not request.user.is_staff:
        return redirect('/')
    if request.method == 'POST':  # If the form has been submitted
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            year_group = form.cleaned_data['year_group']
            tutor_group = form.cleaned_data['tutor_group']
            student = utils.create_student_object(
                first_name,
                last_name,
                year_group,
                tutor_group)
            student.save()
            form = CreateStudentForm()
            return render(request, "student/create.html", {
                'success': " ".join([student.first_name, student.last_name])
                'form': form, },
                context_instance=RequestContext(request))
    else:
        form = CreateStudentForm()  # empty form
    return render(request, 'student/create.html', {
        'form': form,
    }, context_instance=RequestContext(request))