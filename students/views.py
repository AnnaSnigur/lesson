from django.http import HttpResponse, HttpResponseRedirect, \
    HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse

from students.models import Student, Group
from students.forms import StudentsAddForm, GroupsAddForm,  \
    ContactForm


def generate_student(request):
    student = Student.generate_student()
    return HttpResponse(f'{student.get_info()}')


def students(request):
    queryset = Student.objects.all()
    fn = request.GET.get('first_name')
    if fn:
        queryset = queryset.filter(first_name__istartswith=fn)
    return render(request,
                  'student_list.html',
                  context={'student_list': queryset})


def students_add(request):
    if request.method == 'POST':
        form = StudentsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentsAddForm()
    return render(request,
                  'students_add.html',
                  context={'form': form})


def generate_group(request):
    group = Group.generate_student()
    return HttpResponse(f'{group.get_info()}')


def groups(request):
    queryset = Group.objects.all()
    fn = request.GET.get('name')
    if fn:
        queryset = queryset.filter(name__istartswith=fn)
    return render(request,
                  'group_list.html',
                  context={'group_list': queryset})


def groups_add(request):
    if request.method == 'POST':
        form = GroupsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups'))
    else:
        form = GroupsAddForm()
    return render(request,
                  'groups_add.html',
                  context={'form': form})


def students_edit(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return HttpResponseNotFound\
            (f'Student with id {pk} not found')

    if request.method == 'POST':
        form = StudentsAddForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            from django.urls import reverse
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentsAddForm(instance=student)
    return render(request,
                  'students_edit.html',
                  context={'form': form, 'pk': pk})


def groups_edit(request, pk):
    try:
        group = Group.objects.get(id=pk)
    except Group.DoesNotExist:
        return HttpResponseNotFound(f'Groups {pk} not found')

    if request.method == 'POST':
        form = GroupsAddForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            from django.urls import reverse
            return HttpResponseRedirect(reverse('groups'))
    else:
        form = GroupsAddForm(instance=group)
    return render(request,
                  'groups_edit.html',
                  context={'form': form, 'pk': pk})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            from django.urls import reverse
            return HttpResponseRedirect(reverse('students'))
    else:
        form = ContactForm()
    return render(request,
                  'contact.html',
                  context={'form': form})
