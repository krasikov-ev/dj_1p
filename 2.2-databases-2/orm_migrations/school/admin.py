from django.contrib import admin

from .models import Student, Teacher, StudentsTeacher


class StudentsTeacherInline(admin.TabularInline):
    model = StudentsTeacher
    extra = 1


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [StudentsTeacherInline]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [StudentsTeacherInline]




