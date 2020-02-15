from django.http import HttpResponse, HttpResponseRedirect, \
    HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout

from students.models import Student, Group
from students.forms import StudentsAddForm, GroupsAddForm, \
    ContactForm, UserRegistrationForm, UserLoginForm


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
    group = Group.generate_group()
    return HttpResponse(f'{group.get_info()}')


def groups(request):
    queryset = Group.objects.all().select_related('group')
    fn = request.GET.get('name')
    if fn:
        queryset = queryset.filter(name__istartswith=fn)
    return render(request,
                  'group_list.html',
                  context={'groups': queryset})


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
        return HttpResponseNotFound \
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


def register(request):
    user_form = UserRegistrationForm

    if request.method == 'POST':
        form = user_form(request.POST)
        if form.is_valid():
            form.save()
            from django.urls import reverse
            return HttpResponseRedirect(reverse('students'))
    else:
        form = user_form()

    return render(request,
                  'registration.html',
                  context={'form': form})


def custom_login(request):
    user_form = UserLoginForm

    if request.GET.get('logout'):
        logout(request)

    if request.method == 'POST':
        form = user_form(request.POST)
        if form.is_valid():
            user = authenticate(request,
                                username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'],
                                )
            login(request, user)
            from django.urls import reverse
            return HttpResponseRedirect(reverse('students'))
    else:
        form = user_form()

    return render(request,
                  'login.html',
                  context={'form': form})


def handler404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
