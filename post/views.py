import json
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from rest_framework.response import Response
from rest_framework.views import APIView
from HeapExchange.views import LoginRequiredMixin
from .models import Course, Tag, Activity
from .forms import CourseForm, ActivityForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
from post.serializers import CourseSerializer
from django.shortcuts import get_object_or_404
from datetime import datetime


class TempView(TemplateView):
    template_name = 'post/post.html'


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    fields = ['link', 'skill_requirement']
    template_name = "post/course_create_form.html"




@login_required
def create_course(request):
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

            return redirect('posted_course')
    else:
        form = CourseForm()

        return render(request, 'post/course_form.html', {'form': form})


@login_required
def create_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            # do sth
            new_f = form.save(commit=False)
            # initiator
            user = User.objects.get(id=request.user.id)
            new_f.initiator = user
            # initialtime
            new_f.initialtime = datetime.now()
            new_f.save()

            return redirect('posted_activity')
    else:
        form = ActivityForm()

        return render(request, 'post/activity_form.html', {'form': form})



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
    if datetime.date(datetime.now()) >= course.deadline:
        status = 'registering'
    elif datetime.date(datetime.now()) < course.deadline and datetime.date(datetime.now()) > course.time:
        status = 'tobegin'
    else:
        status = 'end'

    return render(request, 'post/course_detail.html', {'course': course,
                                                       'is_self': is_self,
                                                       'has_joined': has_joined,
                                                       'interested': interested, 
                                                       'status' : status,
                                                       })


def activity_detail(request, activity_id):
    activity = Activity.objects.get(id=activity_id)
    if activity.initiator == request.user:
        is_self = True
    else:
        is_self = False
    if request.user in activity.joined.all():
        has_joined = True
    else:
        has_joined = False
    if request.user in activity.interested.all():
        interested = True
    else:
        interested = False
    if datetime.date(datetime.now()) >= course.deadline:
        status = 'registering'
    elif datetime.date(datetime.now()) < course.deadline and datetime.date(datetime.now()) > course.time:
        status = 'tobegin'
    else:
        status = 'end'
    return render(request, 'post/activity_detail.html', {'activity': activity,
                                                       'is_self': is_self,
                                                       'has_joined': has_joined,
                                                       'interested': interested,
                                                       'status': status})




def all_course(request):
    user = request.user
    course_list = Course.objects.exclude(initiator=user)
    return render(request, 'post/all_course.html', {'course_list': course_list})


def all_activity(request):
    user = request.user
    activity_list = Activity.objects.exclude(initiator=user)
    return render(request, 'post/all_activity.html', {'activity_list': activity_list})




@login_required
def posted_course(request):
    user = request.user
    course_list = Course.objects.filter(initiator=user)
    return render(request, 'post/posted_course.html', {'course_list': course_list})


@login_required
def posted_activity(request):
    user = request.user
    activity_list = Activity.objects.filter(initiator=user)
    return render(request, 'post/posted_activity.html', {'activity_list': activity_list})



@login_required
def joined_course(request):
    user = request.user
    course_list = user.c_joins.all()
    return render(request, 'post/joined_course.html', {'course_list': course_list})


@login_required
def joined_activity(request):
    user = request.user
    activity_list = user.a_joins.all()
    return render(request, 'post/joined_activity.html', {'activity_list': activity_list})



@login_required
def interested_course(request):
    user = request.user
    course_list = user.c_interests.all()
    return render(request, 'post/interested_course.html', {'course_list': course_list})


@login_required
def interested_activity(request):
    user = request.user
    activity_list = user.a_interests.all()
    return render(request, 'post/interested_activity.html', {'activity_list': activity_list})



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


@login_required
def join_activity(request, activity_id):
    user = request.user
    activity = activity.objects.get(id=activity_id)
    activity.joined.add(user)
    activity.save()
    return redirect('activity_detail', activity_id=activity_id)


@login_required
def unjoin_activity(request, activity_id):
    user = request.user
    activity = activity.objects.get(id=activity_id)
    activity.joined.remove(user)
    activity.save()
    return redirect('activity_detail', activity_id=activity_id)


@login_required
def interest_activity(request, activity_id):
    user = request.user
    activity = activity.objects.get(id=activity_id)
    activity.interested.add(user)
    activity.save()
    return redirect('activity_detail', activity_id=activity_id)


@login_required
def uninterest_activity(request, activity_id):
    user = request.user
    activity = activity.objects.get(id=activity_id)
    activity.interested.remove(user)
    activity.save()
    return redirect('activity_detail', activity_id=activity_id)


def all_tags(request):
    if 'term' in request.GET:
        tags = Tag.objects.filter(
            name__istartswith=request.GET['term']
        )[:10]
        return HttpResponse(json.dumps([tag.name for tag in tags]))
    return HttpResponse()


@login_required
def update_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    form = CourseForm(request.POST or None, instance=course)
    if form.is_valid():
        form.save()
        return redirect('course_detail', course_id)
    return render(request, 'post/update_course.html', {'form': form, 'course':course})


@login_required
def update_activity(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)
    form = ActivityForm(request.POST or None, instance=activity)
    if form.is_valid():
        form.save()
        return redirect('activity_detail', activity_id)
    return render(request, 'post/update_activity.html', {'form': form, 'activity':activity})


@login_required
def remove_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.delete()
    return redirect('posted_course')

@login_required
def remove_activity(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)
    activity.delete()
    return redirect('posted_activity')



class CourseExploreList(APIView):

    def get(self, request, format=None):
        course = Course.objects.order_by(
            '-time').filter(~Q(initiator=request.user))
        course_url_list = [c.get_absolute_url() for c in course]
        serializer = CourseSerializer(course, many=True)
        for (s, curl) in zip(serializer.data, course_url_list):
            s['url'] = curl

        return Response(serializer.data)



def course_add_tag(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        tags = request.POST.getlist('tags')
            #print tags
        course.tag.clear()
        for tag in tags:
            t, created = Tag.objects.get_or_create(name=tag.lower())
            course.tag.add(t)
        course.save()
        return redirect('course_detail', course_id=course_id)

    else:
        tags = course.tag.all()

    return render(request, 'post/add_tag.html', {'tags':tags})