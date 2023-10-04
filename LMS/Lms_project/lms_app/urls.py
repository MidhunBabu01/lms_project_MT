from django.urls import path
from lms_app import views

app_name = 'lms_app'


urlpatterns = [
    path('',views.index,name='index'),
    path('instructors-register',views.instructors_register,name='instructors_register'),
    path('login',views.login,name='login'),

    path('dashbaord',views.dashbaord,name='dashbaord'),
    path('instructor-course',views.instructor_course,name='instructor_course'),
    
    
    
    
]
