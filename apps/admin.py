from django.contrib import admin

from apps.models import Program, Student, StudentMark, Lecturer, Parent, TuitionFee # import your models here

# Register your models here.
admin.site.register(Program)
admin.site.register(Student)
admin.site.register(StudentMark)
admin.site.register(Lecturer)
admin.site.register(Parent)
admin.site.register(TuitionFee)