from django.urls import path
from lms_app import views

app_name = 'lms_app'


urlpatterns = [
    path('',views.index,name='index'),
    path('instructors-register',views.instructors_register,name='instructors_register'),
    path('student-register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    
    path('dashbaord',views.dashbaord,name='dashbaord'),
    path('instructor-course',views.instructor_course,name='instructor_course'),
    path('create-course',views.create_course,name='create_course'),
    path('edit-course/<int:update_id>/',views.edit_course,name='edit_course'),
    path('delete-course/<int:delete_id>/',views.delete_course,name='delete_course'),
    path('all-courses',views.all_courses,name='all_courses'),
    path('course-details/<int:course_id>/',views.course_details,name='course_details'),

    
]
