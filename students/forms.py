from django.forms import ModelForm, Form, EmailField, CharField, ValidationError
from django.core.mail import send_mail
from django.conf import settings
from django.core.files import File
from django.contrib.auth.models import User

from students.models import Group
from students.models import Student


class BaseStudentForm(ModelForm):
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        email_exists = Student.objects.\
            filter(email__iexact=email).\
            exclude(id=self.instance.id)
        if email_exists.exists():
            raise ValidationError(f'Email {email} is already used')
        return email

    def clean_telephone(self):
        telephone = self.cleaned_data['telephone']
        if not telephone.isdigit():
            raise ValidationError(f'Telephone {telephone} should consist only of numbers')
        telephone_exists = Student.objects.\
            filter(telephone__iexact=telephone).\
            exclude(id=self.instance.id)
        if telephone_exists.exists():
            raise ValidationError(f'Telephone {telephone} is already used')
        return telephone


class StudentsAddForm(BaseStudentForm):
    class Meta:
        model = Student
        fields = '__all__'


class StudentAdminForm(BaseStudentForm):
    class Meta:
        model = Student
        fields = ('id', 'email', 'first_name', 'last_name')


class GroupsAddForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'


class ContactForm(Form):
    email = EmailField()
    subject = CharField()
    text = CharField()

    def save(self):
        data = self.cleaned_data

        subject = data['subject']
        message = data['text']
        email_from = data['email']
        recipient_list = [settings.EMAIL_HOST_USER, ]
        send_mail(subject, message, email_from, recipient_list, fail_silently=False)

        with open(settings.EMAIL_FILE_PATH_REPORT, 'a') as txt:
            file = File(txt)
            file.write(self)


class UserRegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.set_password(self.cleaned_data['password'])
        instance.is_active = False
        super().save(commit)


class UserLoginForm(Form):
    username = CharField()
    password = CharField()