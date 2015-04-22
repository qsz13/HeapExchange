from django.forms import ModelForm, Textarea
from .models import Course
from bootstrap3_datetime.widgets import DateTimePicker


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'location', 'time']
        widgets = {
            # delete datepicker
            #'time': DateTimePicker(options={"format":"YYYY-MM-DD HH:mm","pickSeconds": False},),
            #'description': Textarea(attrs = {'cols' : 80, 'rows' : 20}),
        }