from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Course, Student


class IndexView(TemplateView):
    template_name = 'course_manager/index.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_list'] = Student.objects.all()
        context['course_list'] = Course.objects.all()
        
        return context
    
class AddStudentView(CreateView):
    model = Student
    fields = ['student_name', 'student_surname']
    def get_success_url(self):
        return reverse('course_manager:index')
    
class EditStudentView(UpdateView):
    model = Student
    fields = ['student_name', 'student_surname']
    
    def get_success_url(self):
        return reverse('course_manager:index') 
    
class StudentDetailView(generic.DetailView):
    model = Student
    template_name = 'course_manager/detail_student.html'

class DeleteStudentView(generic.DeleteView):
    model = Student
    template_name = 'course_manager/detail_student.html'
    
    def get_success_url(self):
        return reverse('course_manager:index')   

class EnrollStudentView(TemplateView):
    model = Student
    template_name = 'course_manager/enroll.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_list'] = Student.objects.all()
        context['course_list'] = Course.objects.all()
        
        return context


def enroll_in_course(request):
    
    coursename = request.POST.get('course_name')
    studentid = request.POST.get('student_id')
    course = Course.objects.get(course_name=coursename)
    course.enrolled_students.add(Student.objects.get(student_id=studentid))
    
    return HttpResponseRedirect(reverse('course_manager:index'))

class AddCourseView(CreateView):
    model = Course
    fields = ['course_name']
    def get_success_url(self):
        return reverse('course_manager:index')

class EditCourseView(UpdateView):
    model = Course
    fields = ['course_name']
    
    def get_success_url(self):
        return reverse('course_manager:index') 
    
class CourseDetailView(generic.DetailView):
    model = Course
    template_name = 'course_manager/detail_course.html'

class DeleteCourseView(generic.DeleteView):
    model = Course
    template_name = 'course_manager/detail_course.html'
    
    def get_success_url(self):
        return reverse('course_manager:index') 