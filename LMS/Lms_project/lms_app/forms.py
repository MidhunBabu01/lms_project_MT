from django import forms
from .models import *


class AddCourse(forms.ModelForm):
    class Meta:
        model = Coursess
        exclude = ['added_by']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'price' : forms.NumberInput(attrs={'class':'form-control'}),
            'img' : forms.ClearableFileInput(attrs={'class':'form-control'}),
            'discount_price' : forms.NumberInput(attrs={'class':'form-control'}),
            'course_categories' : forms.Select(attrs={'class':'form-control'}),
            'about_course': forms.Textarea(attrs={'class':'form-control'}),
        }
