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
def create(request, kind):
    if request.method == 'POST':
        if kind == 'a':
            form = ActivityForm(request.POST)
        else:
            form = CourseForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.initiator = User.objects.get(id=request.user.id)
            new_form.initialtime = datetime.now()
            new_form.save()
            return redirect('posted', kind=kind)
    else:
        if kind == 'a':
            form = ActivityForm()
        else:
            form = CourseForm()
        return render(request, 'post/form.html', {'form': form, 'kind': kind, 'action': 'create'})


@login_required
def detail(request, kind, id):
    if kind == 'a':
        post = Activity.objects.get(id=id)
    elif kind == 'c':
        post = Course.objects.get(id=id)

    initiator = post.initiator
    ini_list = []
    for item in initiator.courses.all():
        if item != post:
            ini_list.append(item)
    for item in initiator.activities.all():
        if item != post:
            ini_list.append(item)

    context_dict = {}
    if initiator == request.user:
        is_self = True
    else:
        is_self = False

    if request.user in post.joined.all():
        has_joined = True
    else:
        has_joined = False

    if request.user in post.interested.all():
        interested = True
    else:
        interested = False

    if datetime.date(datetime.now()) <= post.deadline:
        status = 'registering'
    elif datetime.date(datetime.now()) > post.deadline and datetime.date(datetime.now()) < post.time:
        status = 'tobegin'
    else:
        status = 'end'

    return render(request,
                  'post/detail.html',
                  {'kind': kind, 'post': post, 'list': ini_list, 'is_self': is_self, 'has_joined': has_joined, 'interested': interested, 'status': status})


def all(request, kind='c'):
    if kind == 'a':
        list = Activity.objects.exclude(initiator=request.user)
    elif kind == 'c':
        list = Course.objects.exclude(initiator=request.user)
    return render(request, 'post/all.html', {'list': list, 'kind': kind})


@login_required
def posted(request, kind):
    if kind == 'a':
        list = Activity.objects.filter(initiator=request.user)
    elif kind == 'c':
        list = Course.objects.filter(initiator=request.user)
    return render(request, 'post/posted.html', {'list': list, 'kind': kind})


@login_required
def joined(request, kind):
    if kind == 'a':
        list = request.user.joined_activities.all()
    else:
        list = request.user.joined_courses.all()
    return render(request, 'post/joined.html', {'list': list, 'kind': kind})


@login_required
def interested(request, kind):
    if kind == 'a':
        list = request.user.interested_activities.all()
    else:
        list = request.user.interested_courses.all()
    return render(request, 'post/interested.html', {'list': list, 'kind': kind})


@login_required
def join(request, kind, id):
    if kind == 'a':
        post = get_object_or_404(Activity, id=id)
    else:
        post = get_object_or_404(Course, id=id)
    post.joined.add(request.user)
    post.save()
    return redirect('detail', kind=kind, id=id)


@login_required
def unjoin(request, kind, id):
    if kind == 'a':
        post = get_object_or_404(Activity, id=id)
    else:
        post = get_object_or_404(Course, id=id)
    post.joined.remove(request.user)
    post.save()
    return redirect('detail', kind=kind, id=id)


@login_required
def interest(request, kind, id):
    if kind == 'a':
        post = get_object_or_404(Activity, id=id)
    else:
        post = get_object_or_404(Course, id=id)
    post.interested.add(request.user)
    post.save()
    return redirect('detail', kind=kind, id=id)


@login_required
def uninterest(request, kind, id):
    if kind == 'a':
        post = get_object_or_404(Activity, id=id)
    else:
        post = get_object_or_404(Course, id=id)
    post.interested.remove(request.user)
    post.save()
    return redirect('detail', kind=kind, id=id)


def all_tags(request):
    if 'term' in request.GET:
        tags = Tag.objects.filter(
            name__istartswith=request.GET['term']
        )[:10]
        return HttpResponse(json.dumps([tag.name for tag in tags]))
    return HttpResponse()


@login_required
def update(request, kind, id):
    if kind == 'a':
        post = get_object_or_404(Activity, id=id)
        form = ActivityForm(request.POST or None, instance=post)
    else:
        post = get_object_or_404(Course, id=id)
        form = CourseForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('detail', kind, id)
    return render(request, 'post/form.html', {'form': form, 'post': post, 'kind': kind, 'action': 'update'})


@login_required
def remove(request, kind, id):
    if kind == 'a':
        post = get_object_or_404(Activity, id=id)
    else:
        post = get_object_or_404(Course, id=id)
    post.delete()
    return redirect('posted', kind=kind)


class CourseExploreList(APIView):

    def get(self, request, format=None):
        course = Course.objects.order_by(
            '-time').filter(~Q(initiator=request.user))
        course_url_list = [c.get_absolute_url() for c in course]
        serializer = CourseSerializer(course, many=True)
        for (s, curl) in zip(serializer.data, course_url_list):
            s['url'] = curl

        return Response(serializer.data)


def add_tag(request, kind, id):
    if kind == 'a':
        post = get_object_or_404(Activity, id=id)
    else:
        post = get_object_or_404(Course, id=id)

    if request.method == 'POST':
        tags = request.POST.getlist('tags')
        # print tags
        post.tags.clear()
        for tag in tags:
            t, created = Tag.objects.get_or_create(name=tag.lower())
            post.tags.add(t)
        post.save()
        return redirect('detail', kind=kind, id=id)
    else:
        tags = post.tags.all()

    return render(request, 'post/add_tag.html', {'tags': tags, 'item': post})


def all_tags(request):
    tag_list = Tag.objects.all()
    return render(request, 'post/all_tags.html', {'tag_list': tag_list})


def tag_view(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    list = []
    course_list = Course.objects.filter(tags=tag)
    for course in course_list:
        list.append(course)
    activity_list = Activity.objects.filter(tags=tag)
    for activity in activity_list:
        list.append(activity)

    return render(request, 'post/tag_view.html', {'list': list, 'tag': tag, 'kind': 'c'})