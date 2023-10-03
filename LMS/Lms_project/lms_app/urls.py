from django.urls import path
from lms_app import views
urlpatterns = [
    path('',views.index,name='index')
]
