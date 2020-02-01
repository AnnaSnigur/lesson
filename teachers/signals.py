import string

from django.db.models.signals import pre_save
from django.dispatch import receiver
from teachers.models import Teacher


@receiver(pre_save, sender=Teacher)
def pre_save_student(sender, instance, **kwargs):
    instance.email = instance.email.lower()

    if instance.id is None:
        print('Object is create')
    instance.first_name = string.capwords(instance.first_name)
