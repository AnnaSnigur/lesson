from django.forms import ModelForm
from students.models import Group


class GroupsAddForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

