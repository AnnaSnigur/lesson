from datetime import datetime

from faker import Faker
from django.db import models

'''
CREATE TABLE students_student (
    first_name varchar(20)
);
'''


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    email = models.EmailField()
    telephone = models.CharField(max_length=16)
    # job = models.CharField(max_length=255)

    def get_info(self):
        return f'{self.first_name} {self.last_name} {self.birth_date} {self.email}{self.telephone}'

    @classmethod
    def generate_teacher(cls):
        fake = Faker()
        teacher = cls(
            first_name=fake.first_name(),
            birth_date=fake.date_of_birth(),
            last_name=fake.last_name(),
            email=fake.email(),
            telephone=fake.phone_number(),
        )
        teacher.save()
        return teacher

