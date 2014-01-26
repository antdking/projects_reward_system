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
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            is_staff = form.cleaned_data['is_staff']
            user = utils.create_teacher_object(
                first_name,
                last_name,
                admin=is_staff)
            user.save()
            return render(request, "create_teacher/create.html", {
                'success': user.username, })
    else:
        form = CreateTeacherForm()  # empty form
    return render(request, 'create_teacher/create.html', {
        'form': form,
    })
