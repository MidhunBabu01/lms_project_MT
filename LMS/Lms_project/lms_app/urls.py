from django.urls import path
from lms_app import views

app_name = 'lms_app'


urlpatterns = [
    path('',views.index,name='index')
    
]
