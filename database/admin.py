from django.contrib import admin
from .models import Department, Student, Professor, Course, Grade
# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'head_id')

class StudentAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'take_course', 'advisor', 'department')

class ProfessorAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'department')

class CourseAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'department', 'teacher')	

class GradeAdmin(admin.ModelAdmin):
	list_display = ('id', 'student', 'course', 'grade')	

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Grade, GradeAdmin)


