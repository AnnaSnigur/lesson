from django.urls import path

from students.views import (
    generate_student, students,
    students_add, groups, groups_add, students_edit,
    contact,  groups_edit, register, custom_login,
)

urlpatterns = [
    path('gen/', generate_student),
    path('list/', students, name='students'),
    path('add/', students_add, name='students_add'),
    path('groups/', groups, name='groups'),
    path('groups/add/', groups_add, name='groups_add'),
    path('edit/<int:pk>/', students_edit, name='students-edit'),
    path('group_edit/<int:pk>/', groups_edit, name='groups-edit'),
    path('contact/', contact, name='contact'),
    path('register/', register, name='register'),
    path('login/', custom_login, name='login'),
]

