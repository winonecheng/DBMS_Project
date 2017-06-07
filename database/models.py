from django.db import models

# Create your models here.

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    head = models.ForeignKey('Professor', models.SET_NULL, blank=True, null=True, related_name='dp')

    def __str__(self):
        return self.name

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    take_course = models.ForeignKey('Course', models.SET_NULL, blank=True, null=True)
    advisor = models.ForeignKey('Professor', models.SET_NULL, blank=True, null=True)
    department = models.ForeignKey('Department', models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return '{name} ({id})'.format(
            name=self.name,
            id=self.id
        )

class Professor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey('Department', models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return '{name} ({department})'.format(
            name=self.name,
            department=self.department
        )

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey('Department', models.SET_NULL, blank=True, null=True)
    teacher = models.ForeignKey('Professor', models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return '{name} ({department})'.format(
            name=self.name,
            department=self.department
        )

class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey('Student', models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey('Course', models.SET_NULL, blank=True, null=True)
    grade = models.FloatField(default=0.0)

    def __str__(self):
        return '{name} {course}'.format(
            name=self.student,
            course=self.course
        )