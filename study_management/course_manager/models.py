from django.db import models
from django.forms import ModelForm
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=20)
    student_surname = models.CharField(max_length=20)
    
    def __str__(self):
        return self.student_name + " " + self.student_surname + ", StudentID:  " + str(self.student_id)
    
    def getId(self):
        return self.student_id
    
    
class Course(models.Model):
    course_name = models.CharField(max_length=20)
    enrolled_students = models.ManyToManyField(Student)
    
    def __str__(self):
        return self.course_name
    
    