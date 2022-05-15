from django.urls import path

from . import views

app_name = 'course_manager'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add_student', views.AddStudentView.as_view(), name='add_student'),
    path('edit_student/(?P<pk>[0-9]+)/$', views.EditStudentView.as_view(), name='edit_student'),
    path('delete_student/(?P<pk>[0-9]+)/delete', views.DeleteStudentView.as_view(), name='delete_student'),
    path('<int:pk>/', views.StudentDetailView.as_view(), name='detail_student'),
    path('enroll/<int:pk>/', views.EnrollStudentView.as_view(), name='enroll_student'),
    path('enroll/', views.enroll_in_course, name='enroll_in_course'),
    path('add_course', views.AddCourseView.as_view(), name='add_course'),
    path('edit_course/(?P<pk>[0-9]+)/$', views.EditCourseView.as_view(), name='edit_course'),
    path('delete_course/(?P<pk>[0-9]+)/delete', views.DeleteCourseView.as_view(), name='delete_course'),
    path('course/<int:pk>', views.CourseDetailView.as_view(), name='detail_course'),
]
