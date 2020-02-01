from django.urls import path

from teachers.views import teachers, teachers_add, teachers_edit, contact

urlpatterns = [
    path('list/', teachers, name='teachers'),
    path('add/', teachers_add, name='teachers_add'),
    path('edit/<int:pk>/', teachers_edit, name='teachers-edit'),
    path('contact/', contact, name='contact'),
]

