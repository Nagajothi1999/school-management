from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('admin-home', views.admin_home, name='admin_home'),
    path('staff-home', views.staff_home, name='staff_home'),
    path('student-home', views.student_home, name='student_home'),
    path('editor-home', views.editor_home, name='editor_home'),

]