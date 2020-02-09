from django.forms import ModelForm, Form, EmailField, CharField, ValidationError
from django.core.mail import send_mail
from django.conf import settings
from django.core.files import File
from teachers.models import Teacher


class BaseTeacherForm(ModelForm):
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        email_exists = Teacher.objects. \
            filter(email__iexact=email). \
            exclude(id=self.instance.id)
        if email_exists.exists():
            raise ValidationError(f'Email {email} is already used')
        return email

    def clean_telephone(self):
        telephone = self.cleaned_data['telephone']
        if not telephone.isdigit():
            raise ValidationError(f'Telephone {telephone} should consist only of numbers')
        telephone_exists = Teacher.objects. \
            filter(telephone=telephone). \
            exclude(id=self.instance.id)
        if telephone_exists.exists():
            raise ValidationError(f'Telephone {telephone} is already used')
        return telephone


class TeachersAddForm(BaseTeacherForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherAdminForm (BaseTeacherForm):
    class Meta:
        model = Teacher
        fields = ('id', 'email', 'first_name', 'last_name')


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

        with open(settings.EMAIL_FILE_PATH_REPORT, 'w') as txt:
            file = File(txt)
            file.write(self)
        txt.closed

