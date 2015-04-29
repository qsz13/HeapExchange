from django.forms import ModelForm, Textarea
from .models import Course, Activity
from bootstrap3_datetime.widgets import DateTimePicker
from django import forms
from functools import partial

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'location', 'time', 'deadline', 'description', 'requirement', 'limit', 'price']
        widgets = {
        	'title' : forms.TextInput(),
            'time' : DateInput(),
            'deadline' : DateInput(),
            'limit' : forms.NumberInput(),
            'description' : Textarea(attrs = {'cols' : 80, 'rows' : 20, 'class':'materialize-textarea'}),
            'price' : forms.NumberInput(),
        }


class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['title', 'location', 'time', 'deadline', 'description', 'requirement', 'limit']
        widgets = {
            'title' : forms.TextInput(),
            'time' : DateInput(),
            'deadline' : DateInput(),
            'limit' : forms.NumberInput(),
            'description' : Textarea(attrs = {'cols' : 80, 'rows' : 20, 'class':'materialize-textarea'}),
        }