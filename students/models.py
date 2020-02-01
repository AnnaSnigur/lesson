from faker import Faker
from django.db import models
from mimesis import Generic, Person

'''
CREATE TABLE students_student (
    first_name varchar(20)
);
'''


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    date = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=16, unique=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    group = models.ForeignKey('students.Group',
                              null=True, blank=True,
                              on_delete=models.CASCADE)

    def get_info(self):
        return f'{self.first_name}{self.last_name} {self.email}'

    @classmethod
    def generate_student(cls):
        fake = Faker()
        g = Generic('en')
        person = Person('en')
        student = cls(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            date=g.datetime.date(),
            email=fake.email(),
            telephone=person.telephone(),
            address=fake.address(),
        )
        student.save()
        return student

    def __str__(self):
        return f'{self.id} {self.full_name}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Group(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    blood = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=30)
    headman = models.ForeignKey('students.Student',
                                null=True, blank=True,
                                on_delete=models.CASCADE,
                                related_name='+')
    curator = models.ForeignKey('teachers.Teacher',
                                null=True, blank=True,
                                on_delete=models.CASCADE,
                                related_name='+')

    def get_info(self):
        return f'{self.name} {self.email}{self.blood}{self.phone_number} {self.headman} {self.curator}'

    @classmethod
    def generate_group(cls):
        person = Person('en')
        group = cls(
            name=person.full_name(),
            email=person.email(),
            blood=person.blood_type(),
            phone_number=person.telephone(),
        )
        group.save()
        return group

    def __str__(self):
        return f'{self.id} {self.name}'
