from django.urls import path
from lms_app import views

app_name = 'lms_app'


urlpatterns = [
    path('',views.index,name='index'),
    path('instructors-register',views.instructors_register,name='instructors_register'),
    path('login',views.login,name='login'),

    path('dashbaord',views.dashbaord,name='dashbaord'),
    path('instructor-course',views.instructor_course,name='instructor_course'),
    path('create-course',views.create_course,name='create_course'),
    path('edit-course/<int:update_id>/',views.edit_course,name='edit_course'),
    path('delete-course/<int:delete_id>/',views.delete_course,name='delete_course'),

    
    
    
    
    
]
