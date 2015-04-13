from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, CreateView
from HeapExchange.views import LoginRequiredMixin
from post.models import Course


class TempView(TemplateView):
    template_name = 'post/post.html'

class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    fields=['link','skill_requirement']
    template_name = "post/course_create_form.html"