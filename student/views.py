from django.contrib.auth.decorators import login_required
from django.db.models import Q
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
                'success': " ".join([student.first_name, student.last_name]),
                'form': form, },
                context_instance=RequestContext(request))
    else:
        form = CreateStudentForm()  # empty form
    return render(request, 'student/create.html', {
        'form': form,
    }, context_instance=RequestContext(request))


@login_required()
def view_students(request):
    query = request.GET.get('q')
    if query:
        if ' ' in query:
            query = query.split(' ')
            student_list = Student.objects.filter(Q(first_name__icontains=query[0]) |
                                                  Q(last_name__icontains=query[0]),
                                                  Q(first_name__icontains=query[1]) |
                                                  Q(last_name__icontains=query[1]))
        else:
            student_list = Student.objects.filter(Q(first_name__icontains=query) |
                                                  Q(last_name__icontains=query))
    else:
        student_list = Student.objects.order_by('last_name')
    context = {'students': student_list}
    return render(request, 'student/student_list.html',
                  context, context_instance=RequestContext(request))