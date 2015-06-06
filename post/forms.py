from django.forms import ModelForm, Textarea
from .models import Course, Activity, Post, OneTimeSchedule, SequenceTimeSchedule, WeeklyTimeSchedule, Arrangement
from django import forms
from functools import partial
from .models import CourseBulletin, ActivityBulletin

# DateInput = partial(forms.DateInput, {'class': 'datepicker', 'type': 'date'})


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'schedule_type','deadline', 'location', 'description',
                  'requirement', 'limit', 'price']
        widgets = {
            'title': forms.TextInput(),
            'schedule_type': forms.Select(choices=Post.SCHEDULE_TYPE),
            'limit': forms.NumberInput(),
            'description': Textarea(attrs={'cols': 80, 'rows': 20, 'class': 'materialize-textarea'}),
            'price': forms.NumberInput(),
            'deadline':forms.DateInput(attrs={'class': 'datepicker'}),
        }



class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['title', 'schedule_type','deadline', 'location', 'description', 'requirement', 'limit']
        widgets = {
            'title': forms.TextInput(),
            'schedule_type': forms.Select(choices=Post.SCHEDULE_TYPE),
            'limit': forms.NumberInput(),
            'description': Textarea(attrs={'cols': 80, 'rows': 20, 'class': 'materialize-textarea'}),
             'deadline':forms.DateInput(attrs={'class': 'datepicker'}),
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
            'sequence_start_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'sequence_end_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'sequence_start_time': forms.TimeInput(attrs={'class': 'timepicker'}),
            'sequence_end_time': forms.TimeInput(attrs={'class': 'timepicker'}),
        }



class WeeklyTimeForm(ModelForm):
    class Meta:
        model = WeeklyTimeSchedule
        fields = '__all__'

        widgets = {
             'weekly_start_date': forms.DateInput(attrs={'class': 'datepicker'}),
             'weekly_end_date': forms.DateInput(attrs={'class': 'datepicker'}),
             'weekly_start_time': forms.TimeInput(attrs={'class': 'timepicker'}),
             'weekly_end_time': forms.TimeInput(attrs={'class': 'timepicker'}),
        }


class CourseBulletinForm(ModelForm):
    class Meta:
        model = CourseBulletin
        fields = ['content',]
        widgets = {
                'content' : Textarea(attrs={'class': 'materialize-textarea'}),
        }

class ActivityBulletinForm(ModelForm):
    class Meta:
        model = ActivityBulletin
        fields = ['content']
        widgets = {
                'content' : Textarea(attrs={'class': 'materialize-textarea'}),
        }