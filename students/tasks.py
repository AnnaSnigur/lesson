from celery import shared_task
from datetime import datetime, timedelta

from students.models import Student, Logger


@shared_task
def add(x, y):
    print('Student.objects.count()')
    print(Student.objects.count())
    return x + y


@shared_task
def clear_log():
    d = datetime.today() - timedelta(days=1)
    Logger.objects.filter(created__lt=d).delete()

