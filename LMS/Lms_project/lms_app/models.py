from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course_catg(models.Model):
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Course Categories'
    name = models.CharField(max_length=250)
    


class Coursess(models.Model):
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Courses'
    added_by = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    img = models.ImageField(upload_to='pictures',blank=True,null=True)
    discount_price = models.IntegerField()
    course_categories = models.ForeignKey(Course_catg,on_delete=models.CASCADE)
    about_course = models.TextField()