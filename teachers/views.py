from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse

from teachers.models import Teacher
from teachers.forms import TeachersAddForm,  ContactForm


def generate_teacher(request):
    teacher = Teacher.generate_teacher()
    return HttpResponse(f'{teacher.get_info()}')


def teachers(request):
    queryset = Teacher.objects.all()
    fn = request.GET.get('first_name')
    if fn:
        queryset = queryset.filter(
            Q(first_name__istartswith=fn) | Q(last_name__istartswith=fn) | Q(email__istartswith=fn))
    return render(request,
                  'teachers_list.html',
                  context={'teachers_list': queryset})


def teachers_add(request):
    if request.method == 'POST':
        form = TeachersAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers'))
    else:
        form = TeachersAddForm()

    return render(request,
                  'teachers_add.html',
                  context={'form': form})


def teachers_edit(request, pk):
    try:
        teacher = Teacher.objects.get(id=pk)
    except Teacher.DoesNotExist:
        return HttpResponseNotFound(f'Teacher {pk} not found')

    if request.method == 'POST':
        form = TeachersAddForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            from django.urls import reverse
            return HttpResponseRedirect(reverse('groups'))
    else:
        form = TeachersAddForm(instance=teacher)

    return render(request,
                  'teachers_edit.html',
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

