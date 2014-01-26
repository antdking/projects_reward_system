from django.shortcuts import render
from django import forms
from create_teacher import utils


class CreateTeacherForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    is_staff = forms.BooleanField(required=False)


def create_teacher(request):
    if request.method == 'POST':  # If the form has been submitted
        form = CreateTeacherForm(request.POST)
        if form.is_valid():
            user = utils.create_teacher_object(
                form.first_name,
                form.last_name,
                admin=form.is_staff)
            user.save()
            return render(request, "create_teacher/create.html", {
                'success': user.username, })
    else:
        form = CreateTeacherForm()  # empty form
    return render(request, 'create_teacher/create.html', {
        'form': form,
    })
