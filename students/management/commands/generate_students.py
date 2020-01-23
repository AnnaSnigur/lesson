from django.core.management.base import BaseCommand, CommandError
from students.models import Student, Group
from teachers.models import Teacher
import random


class Command(BaseCommand):
    help = 'Generate random students'

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--number',
            help='Delete poll instead of closing it',
        )

    def handle(self, *args, **options):
        number = int(options.get('number') or 100)
        for _ in range(number):
            Student.generate_student()

    def handle(self, *args, **options):
        groups = list(Group.objects.all())
        students = list(Student.objects.all())
        teachers = list(Teacher.objects.all())

        for student in Student.objects.all():
            student.group = random.choice(groups)
            student.save()

        for group in Group.objects.all():
            group.headman = random.choice(students)
            group.curator = random.choice(teachers)
            group.save()
