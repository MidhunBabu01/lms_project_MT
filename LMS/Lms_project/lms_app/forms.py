from django import forms
from .models import *


class AddCourse(forms.ModelForm):
    class Meta:
        model = Coursess
        exclude = ['added_by']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control','required':'required'}),
            'price' : forms.NumberInput(attrs={'class':'form-control','required':'required'}),
            'img' : forms.ClearableFileInput(attrs={'class':'form-control','required':'required'}),
            'discount_price' : forms.NumberInput(attrs={'class':'form-control','required':'required'}),
            'course_categories' : forms.Select(attrs={'class':'form-control','required':'required'}),
            'about_course': forms.Textarea(attrs={'class':'form-control'}),
        }
