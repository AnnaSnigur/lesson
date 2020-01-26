from django.contrib import admin

from teachers.models import Teacher
from students.admin import GroupInline


class TeacherAdmin(admin.ModelAdmin):
    readonly_fields = ('email',)
    list_display = ('id', 'first_name', 'last_name', 'email', 'birth_date')
    list_per_page = 10
    inlines = [GroupInline, ]

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if request.user.groups.filter(name='manager').exists():
            return readonly_fields + ('telephone',)
        return readonly_fields


admin.site.register(Teacher, TeacherAdmin)
