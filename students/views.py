from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from students.models import Student, Group
from students.forms import GroupsAddForm


def generate_student(request):
    student = Student.generate_student()
    return HttpResponse(f'{student.get_info()}')


def students(request):
    queryset = Student.objects.all()
    response = ''

    print("request.GET.get('first_name')")
    fn = request.GET.get('first_name')
    if fn:
        # __contains LIKE %{}%
        # queryset = queryset.filter(first_name__contains=fn)

        # __endswith  LIKE %{}
        # queryset = queryset.filter(first_name__endswith=fn)

        # __startswith  LIKE {}%
        queryset = queryset.filter(first_name__istartswith=fn)

    for student in queryset:
        response += student.get_info() + '<br>'
        # response = response + student.get_info() + '<br>'
    print('queryset.query')
    print(queryset.query)
    return render(request,
                  'student_list.html',
                  context={'student_list': response})


def generate_group(request):
    group = Group.generate_student()
    return HttpResponse(f'{group.get_info()}')


def groups(request):
    queryset = Group.objects.all()
    response = ''

    print("request.GET.get('name')")
    fn = request.GET.get('name')
    if fn:
        queryset = queryset.filter(name__istartswith=fn)

    for group in queryset:
        response += group.get_info() + '<br>'
    print('queryset.query')
    print(queryset.query)
    return render(request,
                  'group_list.html',
                  context={'group_list': response})


def groups_add(request):
    if request.method == 'POST':
        form = GroupsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')
    else:
        form = GroupsAddForm()

    return render(request,
                  'groups_add.html',
                  context={'form': form})

