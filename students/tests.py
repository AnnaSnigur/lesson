from django.test import TestCase
from students.models import Student


class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(first_name='John', last_name='Davis',
                               date='01/01/1999', email='adam38@yahoo.com',
                               telephone='1111111111', address='New York',)

    def test_student(self):
        student = Student.objects.get(last_name='Davis')
        self.assertEqual(student.get_info(), 'Student')
