from django.forms import ModelForm, Form, EmailField, CharField
from django.core.mail import send_mail
from django.conf import settings
from django.core.files import File

from students.models import Group
from students.models import Student


class StudentsAddForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


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
