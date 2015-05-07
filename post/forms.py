from django.forms import ModelForm, Textarea
from .models import Course, Activity, Post, OneTimeSchedule, SequenceTimeSchedule, WeeklyTimeSchedule
from django import forms
from functools import partial

# DateInput = partial(forms.DateInput, {'class': 'datepicker', 'type': 'date'})


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'schedule_type', 'location', 'description',
                  'requirement', 'limit',
                  'price']
        widgets = {
            'title': forms.TextInput(),
            'schedule_type': forms.Select(choices=Post.SCHEDULE_TYPE),
            'limit': forms.NumberInput(),
            'description': Textarea(attrs={'cols': 80, 'rows': 20, 'class': 'materialize-textarea'}),
            'price': forms.NumberInput(),
        }


class OneTimeForm(ModelForm):
    class Meta:
        model = OneTimeSchedule
        fields = '__all__'

        widgets = {
            'once_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'once_start_time': forms.TimeInput(attrs={'class': 'timepicker'}),
            'once_end_time': forms.TimeInput(attrs={'class': 'timepicker'}),
        }


class SequenceTimeForm(ModelForm):
    class Meta:
        model = SequenceTimeSchedule
        fields = '__all__'

        widgets = {
            'start_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'end_date': forms.DateInput(attrs={'class': 'datepicker'}),
        }


class WeeklyTimeForm(ModelForm):
    class Meta:
        model = WeeklyTimeSchedule
        fields = '__all__'


class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['title', 'location', 'description', 'requirement', 'limit']
        widgets = {
            'title': forms.TextInput(),
            'limit': forms.NumberInput(),
            'description': Textarea(attrs={'cols': 80, 'rows': 20, 'class': 'materialize-textarea'}),
        }
