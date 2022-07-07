from django import forms
from django.forms import ModelForm
from .models import Task

#create a Task form

class TaskForm(ModelForm):
    class Meta:
        model=Task
        fields=('title','description')
        labels={
            'title':'Title',
            'description':'Description',
        }
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the title'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter the Desctiption'}),
        }