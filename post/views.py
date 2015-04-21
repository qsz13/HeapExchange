from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from HeapExchange.views import LoginRequiredMixin
from .models import Course
from .forms import CourseForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime


class TempView(TemplateView):
    template_name = 'post/post.html'


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    fields = ['link', 'skill_requirement']
    template_name = "post/course_create_form.html"


@login_required
def get_course_form(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            # do sth
            new_f = form.save(commit=False)
            # initiator
            user = User.objects.get(id=request.user.id)
            new_f.initiator = user
            # initialtime
            new_f.initialtime = datetime.now()
            new_f.save()

            return HttpResponse("success")
    else:
        form = CourseForm()

        return render(request, 'post/course_form.html', {'form': form})


@login_required
def posted_course(request):
	user = request.user
	course_list = Course.objects.filter(initiator=user)
	
	return render(request, 'post/posted_course.html', {'course_list' : course_list})


def all_course(request):
	course_list = Course.objects.all()
	
	return render(request, 'post/all_course.html', {'course_list' : course_list})


@login_required
def join_course(request, course_id):
	user = request.user
	course = Course.objects.get(id=course_id)
	course.joined.add(user)
	course.save()

	return redirect('all_course')
