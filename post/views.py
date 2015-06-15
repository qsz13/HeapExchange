#!/usr/bin/python
# -*- coding: utf-8 -*-


from PIL import Image
from StringIO import StringIO
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView
from coin.models import transfer
from .models import Course, Tag, Activity, Arrangement, CourseImages, ActivityImages
from .forms import CourseForm, ActivityForm, OneTimeForm, SequenceTimeForm
from .forms import WeeklyTimeForm, CourseBulletinForm, ActivityBulletinForm
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from notifications import notify
from post.serializers import CourseSerializer
from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta
from django.forms.models import modelformset_factory
from .helpers import DateJudge
from postman.api import pm_write
from .helpers import noti

class TempView(TemplateView):
    template_name = 'post/post.html'


# class CourseCreateView(LoginRequiredMixin, CreateView):
# model = Course
# fields = ['link', 'skill_requirement']
# template_name = "post/course_create_form.html"


@login_required
def create(request, kind):
    once_form = OneTimeForm()
    sequence_form = SequenceTimeForm()
    weekly_form = WeeklyTimeForm()
    if request.method == 'POST':
        if kind == 'a':
            form = ActivityForm(request.POST)
        else:
            form = CourseForm(request.POST)
        if form.is_valid():
            once_schedule = None
            sequence_schedule = None
            weekly_schedule = None
            if request.POST['schedule_type'] == 'ONCE':
                once_form = OneTimeForm(request.POST)
                if once_form.is_valid():
                    once_schedule = once_form.save()
                else:
                    return render(request, 'post/form.html',
                                  {'form': form, 'once_form': once_form, 'sequence_form': sequence_form,
                                   'weekly_form': weekly_form,
                                   'kind': kind, 'action': 'create'})

            elif request.POST['schedule_type'] == "SEQU":
                sequence_form = SequenceTimeForm(request.POST)
                if sequence_form.is_valid():
                    sequence_schedule = sequence_form.save()
                else:
                    return render(request, 'post/form.html',
                                  {'form': form, 'once_form': once_form, 'sequence_form': sequence_form,
                                   'weekly_form': weekly_form,
                                   'kind': kind, 'action': 'create'})
            elif request.POST['schedule_type'] == "WEEK":
                weekly_form = WeeklyTimeForm(request.POST)
                if weekly_form.is_valid():
                    weekly_schedule = weekly_form.save()
                else:
                    return render(request, 'post/form.html',
                                  {'form': form, 'once_form': once_form, 'sequence_form': sequence_form,
                                   'weekly_form': weekly_form,
                                   'kind': kind, 'action': 'create'})

            new_post = form.save(commit=False)
            new_post.initiator = User.objects.get(id=request.user.id)
            new_post.initialtime = datetime.now()
            if request.POST['schedule_type'] == 'ONCE':
                new_post.one_time_schedule = once_schedule
            elif request.POST['schedule_type'] == "SEQU":
                new_post.sequence_time_schedule = sequence_schedule
            elif request.POST['schedule_type'] == "WEEK":
                new_post.weekly_time_schedule = weekly_schedule
            new_post.save()

            if kind == 'c' and request.POST['schedule_type'] == "SEQU":
                start = new_post.sequence_time_schedule.sequence_start_date
                end = new_post.sequence_time_schedule.sequence_end_date
                date_order = 0
                length = (end - start).days + 1
                for day in range(length):
                    arrange = Arrangement.objects.create()
                    arrange.course = new_post
                    arrange.order = date_order
                    arrange.time = start + timedelta(days=date_order)  # day
                    date_order += 1
                    arrange.content = ''
                    arrange.save()
                    print 'arr' + str(arrange.time)

            if kind == 'c' and request.POST['schedule_type'] == "WEEK":
                start = new_post.weekly_time_schedule.weekly_start_date
                end = new_post.weekly_time_schedule.weekly_end_date
                date_order = 0
                week_list = []
                if new_post.weekly_time_schedule.monday:
                    week_list.append(True)
                else:
                    week_list.append(False)
                if new_post.weekly_time_schedule.tuesday:
                    week_list.append(True)
                else:
                    week_list.append(False)
                if new_post.weekly_time_schedule.wednesday:
                    week_list.append(True)
                else:
                    week_list.append(False)
                if new_post.weekly_time_schedule.thursday:
                    week_list.append(True)
                else:
                    week_list.append(False)
                if new_post.weekly_time_schedule.friday:
                    week_list.append(True)
                else:
                    week_list.append(False)
                if new_post.weekly_time_schedule.saturday:
                    week_list.append(True)
                else:
                    week_list.append(False)
                if new_post.weekly_time_schedule.sunday:
                    week_list.append(True)
                else:
                    week_list.append(False)

                if week_list[start.weekday()]:
                    week_index = start.weekday()
                else:
                    for i in range(7):
                        if week_list[(start.weekday() + i) % 7]:
                            start = start + timedelta(days=i)

                week_index = start.weekday()
                date_order = 0
                for day in range((end - start).days + 1):
                    if week_list[week_index]:
                        arrange = Arrangement.objects.create()
                        arrange.course = new_post
                        arrange.order = date_order
                        arrange.time = start + timedelta(days=day)  # day
                        date_order += 1
                        arrange.content = ''
                        arrange.save()
                        print 'arr' + str(arrange.time)
                    week_index = (week_index + 1) % 7

            return redirect('post:posted', kind=kind)
        else:
            return render(request, 'post/form.html',
                          {'form': form, 'once_form': once_form, 'sequence_form': sequence_form,
                           'weekly_form': weekly_form,
                           'kind': kind, 'action': 'create'})
    else:
        if kind == 'a':
            form = ActivityForm()
        else:
            form = CourseForm()

        return render(request, 'post/form.html',
                      {'form': form, 'once_form': once_form, 'sequence_form': sequence_form, 'weekly_form': weekly_form,
                       'kind': kind, 'action': 'create'})


@login_required
def detail(request, kind, post_id):
    post = None
    try:
        if kind == 'a':
            post = Activity.objects.get(id=post_id)
        elif kind == 'c':
            post = Course.objects.get(id=post_id)
    except ObjectDoesNotExist:
        raise Http404("post does not exist")

    initiator = post.initiator
    ini_list = []
    for item in initiator.courses.all():
        if item != post:
            ini_list.append(item)
    for item in initiator.activities.all():
        if item != post:
            ini_list.append(item)

    if initiator == request.user:
        is_self = True
    else:
        is_self = False

    if request.user in post.joined.all():
        has_joined = True
    else:
        has_joined = False
    if request.user in post.interested.all():
        interested_post = True
    else:
        interested_post = False

    schedule = post.get_post_schedule()
    if post.limit <= post.joined.count():
        status = 'full'
    elif datetime.date(datetime.now()) <= post.deadline:
        status = 'registering'
    elif post.deadline < datetime.date(datetime.now()) < DateJudge(post).start_date:
        status = 'tobegin'
    elif DateJudge(post).start_date <= datetime.now().date() <= DateJudge(post).end_date:
        status = 'ing'
    else:
        status = 'end'


    if kind == 'a':
        post = Activity.objects.get(id=post_id)

    elif kind == 'c':
        post = Course.objects.get(id=post_id)
    image_set = post.images.all()

    return render(request,
                  'post/detail.html',
                  {'kind': kind, 'post': post, 'schedule': schedule, 'list': ini_list, 'is_self': is_self,
                   'has_joined': has_joined,
                   'interested': interested_post, 'status': status,'images':image_set})


def all_post(request, kind='c'):
    activity_list = []
    if kind == 'a':
        activity_list = Activity.objects.exclude(initiator=request.user)
    elif kind == 'c':
        activity_list = Course.objects.exclude(initiator=request.user)
    return render(request, 'post/all.html', {'list': activity_list, 'kind': kind})


@login_required
def posted(request, kind):
    posted_list = []
    if kind == 'a':
        posted_list = Activity.objects.filter(initiator=request.user)
    elif kind == 'c':
        posted_list = Course.objects.filter(initiator=request.user)
    return render(request, 'post/posted.html', {'list': posted_list, 'kind': kind, 'is_posted': True})


@login_required
def joined(request, kind):
    if kind == 'a':
        joined_list = request.user.joined_activities.all()
    else:
        joined_list = request.user.joined_courses.all()
    return render(request, 'post/joined.html', {'list': joined_list, 'kind': kind})


@login_required
def interested(request, kind):
    if kind == 'a':
        interest_list = request.user.interested_activities.all()
    else:
        interest_list = request.user.interested_courses.all()
    return render(request, 'post/interested.html', {'list': interest_list, 'kind': kind})


@login_required
def join(request, kind, post_id):
    if kind == 'a':
        post = get_object_or_404(Activity, id=post_id)
    else:
        post = get_object_or_404(Course, id=post_id)

    if kind == 'c':
        if transfer(from_user=request.user, to_user=post.initiator, amount=post.price):

            post.joined.add(request.user)
            post.save()

            noti_content = u'报名参加你的课程' + post.title
            notify.send(request.user, recipient=post.initiator, verb=noti_content, description=post.get_absolute_url())
    else:
        post.joined.add(request.user)
        post.save()
        noti_content = u'报名参加你的课程' + post.title
        notify.send(request.user, recipient=post.initiator, verb=noti_content, description=post.get_absolute_url())

    return redirect('post:detail', kind=kind, post_id=post_id)


@login_required
def unjoin(request, kind, post_id):
    if kind == 'a':
        post = get_object_or_404(Activity, id=post_id)
    else:
        post = get_object_or_404(Course, id=post_id)
    post.joined.remove(request.user)
    post.save()
    noti_content = u'退出了你的课程' + post.title
    notify.send(request.user, recipient=post.initiator, verb=noti_content, description=post.get_absolute_url())
    if kind == 'c':
        transfer(from_user=post.initiator, to_user=request.user, amount=post.price)
    return redirect('post:detail', kind=kind, post_id=post_id)


@login_required
def interest(request, kind, post_id):
    if kind == 'a':
        post = get_object_or_404(Activity, id=post_id)
    else:
        post = get_object_or_404(Course, id=post_id)
    post.interested.add(request.user)
    post.save()
    return redirect('post:detail', kind=kind, post_id=post_id)


@login_required
def uninterest(request, kind, post_id):
    if kind == 'a':
        post = get_object_or_404(Activity, id=post_id)
    else:
        post = get_object_or_404(Course, id=post_id)
    post.interested.remove(request.user)
    post.save()
    return redirect('post:detail', kind=kind, post_id=post_id)


def all_tags(request):
    tag_list = Tag.objects.all()
    return render(request, 'post/all_tags.html', {'tag_list': tag_list})


@login_required
def update(request, kind, post_id):
    if kind == 'a':
        post = get_object_or_404(Activity, id=post_id)
        form = ActivityForm(request.POST or None, instance=post)
    else:
        post = get_object_or_404(Course, id=post_id)
        form = CourseForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post:detail', kind=kind, post_id=post_id)

    once_form = OneTimeForm()
    sequence_form = SequenceTimeForm()
    weekly_form = WeeklyTimeForm()

    if post.schedule_type == 'ONCE':
        once_form = OneTimeForm(instance=post.one_time_schedule)
    elif post.schedule_type == 'SEQU':
        sequence_form = SequenceTimeForm(instance=post.sequence_time_schedule)
    elif post.schedule_type == 'WEEK':
        weekly_form = WeeklyTimeForm(instance=post.weekly_time_schedule)

    return render(request, 'post/form.html',
                  {'form': form, 'post': post, 'kind': kind, 'once_form': once_form, 'sequence_form': sequence_form,
                   'weekly_form': weekly_form, 'action': 'update'})


@login_required
def remove(request, kind, post_id):
    if kind == 'a':
        post = get_object_or_404(Activity, id=post_id)
    else:
        post = get_object_or_404(Course, id=post_id)
    post.delete()
    return redirect('post:posted', kind=kind)


class CourseExploreList(APIView):
    @staticmethod
    def get(request):
        course = Course.objects.order_by(
            '-initialtime').filter(~Q(initiator=request.user))
        course_url_list = [c.get_absolute_url() for c in course]
        course_schedule_list = [c.get_post_schedule() for c in course]
        serializer = CourseSerializer(course, many=True)
        for (s, curl) in zip(serializer.data, course_url_list):
            s['url'] = curl

        for (s, schedule) in zip(serializer.data, course_schedule_list):
            s['schedule'] = schedule

        return Response(serializer.data)


def add_tag(request, kind, post_id):
    if kind == 'a':
        post = get_object_or_404(Activity, id=post_id)
    else:
        post = get_object_or_404(Course, id=post_id)

    if request.method == 'POST':
        tags = request.POST.getlist('tags')
        # print tags
        post.tags.clear()
        for tag in tags:
            t, created = Tag.objects.get_or_create(name=tag.lower())
            post.tags.add(t)
        post.save()
        return redirect('post:detail', kind=kind, post_id=post_id)
    else:
        tags = post.tags.all()

    return render(request, 'post/add_tag.html', {'tags': tags, 'item': post})


def tag_view(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    tag_list = []
    course_list = Course.objects.filter(tags=tag)
    for course in course_list:
        tag_list.append(course)
    activity_list = Activity.objects.filter(tags=tag)
    for activity in activity_list:
        tag_list.append(activity)

    return render(request, 'post/tag_view.html', {'list': tag_list, 'tag': tag, 'kind': 'c'})


@login_required
def edit_arrange(request, post_id):
    ArrFormSet = modelformset_factory(Arrangement, fields=('content',))
    if request.method == 'POST':
        formset = ArrFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('post:arrange_detail', post_id)
    else:
        course = Course.objects.get(id=post_id)
        if not course.has_arr:
            course.has_arr = True
            course.save()
        arr_list = course.arrangements.all().order_by('order')
        formset = ArrFormSet(queryset=arr_list)
        time_list = []
        for arr in arr_list:
            time_list.append(arr.time)
        fset_time = zip(formset, time_list)
        return render(request, 'post/edit_arrangement.html', {'formset': formset})


def arrange_detail(request, post_id):
    course = Course.objects.get(id=post_id)
    arr_list = course.arrangements.all().order_by('order')
    is_self = (course.initiator == request.user)
    today = datetime.now().date()
    return render(request, 'post/arrange_detail.html',
                  {'arr_list': arr_list, 'is_self': is_self, 'post_id': post_id, 'today': today})


@login_required
def upload_image(request, kind, post_id):
    if request.method == 'GET':
        if kind == 'a':
            post = Activity.objects.get(id=post_id)

        elif kind == 'c':
            post = Course.objects.get(id=post_id)
        image_set = post.images.all()

        return render(request, 'post/upload_image.html', {"images": image_set,'kind':kind})

    elif request.method == 'POST':
        if request.FILES:
            upload_file = request.FILES['image']
            im = Image.open(StringIO(upload_file.read()))
            file_name = "media/imgs/" + kind + str(post_id) + '-' + upload_file.name
            im.save(file_name, "PNG")
            if kind == 'a':
                post = Activity.objects.get(id=post_id)
                activity_image = ActivityImages.objects.create()
                activity_image.image_file = '/'+file_name
                activity_image.post = post
                activity_image.save()
            elif kind == 'c':
                post = Course.objects.get(id=post_id)
                course_image = CourseImages.objects.create()
                course_image.image_file = '/'+file_name
                course_image.post = post
                course_image.save()

    return redirect('post:upload_image', kind=kind, post_id=post_id)


@login_required
def remove_image(request, kind, img_id):
    post_image = None
    if kind == 'a':
        post_image = ActivityImages.objects.get(id=img_id)


    elif kind == 'c':
        post_image = CourseImages.objects.get(id=img_id)

    post = post_image.post

    if post.initiator == request.user:
        post_image.delete()


    return redirect('post:upload_image', kind=kind, post_id=post.id)



@login_required
def invite(request, kind, post_id):
    if kind == 'a':
        post = Activity.objects.get(id=post_id)

    elif kind == 'c':
        post = Course.objects.get(id=post_id)
    to_user_name = request.GET['invite']
    to_user = User.objects.get(username=to_user_name)
    from_user = request.user
    pm_write(from_user, to_user, u'邀请: '+post.title, body=u'快来参加这个活动吧：<a href="'+post.get_absolute_url()+u'">链接</a>')

    return redirect('post:detail', kind=kind, post_id=post_id)

@login_required
def create_bulletin(request, flag, post_id):
    if flag == 'c':
        Post = Course
        Form = CourseBulletinForm
    else:
        Post = Activity
        Form = ActivityBulletinForm

    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.initiator = request.user
            new_form.post = Post.objects.get(id=post_id)
            new_form.save()
            noti(request.user, new_form.post, new_form.content)
            return redirect('post:view_bulletin', flag, post_id)
    else:
        form = Form()
        return render(request, 'post/create_bulletin.html', {'form':form})

@login_required
def view_bulletin(request, flag, post_id):
    if flag == 'c':
        post = get_object_or_404(Course, id=post_id)
    else:
        post = get_object_or_404(Activity, id=post_id)

    if request.user != post.initiator and request.user not in post.joined.all():
        return redirect('post:detail', kind=flag, post_id=post_id)

    list = post.bulletins.all().order_by('-initial_time')
    return render(request, 'post/view_bulletin.html', {'list':list, 'id':post_id, 'flag':flag})
