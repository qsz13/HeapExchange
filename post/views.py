import json
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from HeapExchange.views import LoginRequiredMixin
from .models import Course, Tag
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
    return render(request, 'post/posted_course.html', {'course_list': course_list})


def all_course(request):
    course_list = Course.objects.all()
    return render(request, 'post/all_course.html', {'course_list': course_list})


@login_required
def join_course(request, course_id):
    user = request.user
    course = Course.objects.get(id=course_id)
    course.joined.add(user)
    course.save()
    return redirect('course_detail', course_id=course_id)


@login_required
def unjoin_course(request, course_id):
    user = request.user
    course = Course.objects.get(id=course_id)
    course.joined.remove(user)
    course.save()
    return redirect('course_detail', course_id=course_id)


@login_required
def interest_course(request, course_id):
    user = request.user
    course = Course.objects.get(id=course_id)
    course.interested.add(user)
    course.save()
    return redirect('course_detail', course_id=course_id)


@login_required
def uninterest_course(request, course_id):
    user = request.user
    course = Course.objects.get(id=course_id)
    course.interested.remove(user)
    course.save()
    return redirect('course_detail', course_id=course_id)


def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    if course.initiator == request.user:
        is_self = True
    else:
        is_self = False
    if request.user in course.joined.all():
        has_joined = True
    else:
        has_joined = False
    if request.user in course.interested.all():
        interested = True
    else:
        interested = False
    return render(request, 'post/course_detail.html', {'course': course,
                                                       'is_self': is_self,
                                                       'has_joined': has_joined,
                                                       'interested': interested})


@login_required
def joined_course(request):
    user = request.user
    course_list = user.joins.all()
    return render(request, 'post/joined_course.html', {'course_list': course_list})


@login_required
def interested_course(request):
    user = request.user
    course_list = user.interests.all()
    return render(request, 'post/interested_course.html', {'course_list': course_list})

def all_tags(request):
    if 'term' in request.GET:
        tags = Tag.objects.filter(
            name__istartswith=request.GET['term']
        )[:10]
        return HttpResponse( json.dumps( [ tag.name for tag in tags ] ) )
    return HttpResponse()