from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q
from teachers.models import Teacher
from teachers.forms import TeachersAddForm


def generate_teacher(request):
    teacher = Teacher.generate_teacher()
    return HttpResponse(f'{teacher.get_info()}')


def teachers(request):
    queryset = Teacher.objects.all()
    response = ''

    print("request.GET.get('first_name')")
    fn = request.GET.get('first_name')
    if fn:
        queryset = queryset.filter(
            Q(first_name__istartswith=fn) | Q(last_name__istartswith=fn) | Q(email__istartswith=fn))

    for teacher in queryset:
        response += teacher.get_info() + '<br>'
    print('queryset.query')
    print(queryset.query)
    return render(request,
                  'teachers_list.html',
                  context={'teachers_list': response})


def teachers_add(request):
    if request.method == 'POST':
        form = TeachersAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')
    else:
        form = TeachersAddForm()

    return render(request,
                  'teachers_add.html',
                  context={'form': form})
