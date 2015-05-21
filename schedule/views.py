from django.shortcuts import render
from django.contrib.auth.models import User
from post.models import Course, Activity, Arrangement
from django.contrib.auth.decorators import login_required
import operator
from datetime import datetime, date, timedelta

class TimelineItem:
	def __init__(self, title, date,  content):
		self.title = title
		self.date = date
		self.content = content


def find(user):
	tl_list = []
	for course in user.courses.all():
		if course.schedule_type == 'ONCE':
			if course.one_time_schedule.once_date >= datetime.now().date():
				tl_list.append(TimelineItem(course.title, course.one_time_schedule.once_date, arr.content))
		else:
			for arr in course.arrangements.all():
				if arr.time >= datetime.now().date():
					tl_list.append(TimelineItem(course.title, arr.time, arr.content))
	for course in user.joined_courses.all():
		if course.schedule_type == 'ONCE':
			if course.one_time_schedule.once_date >= datetime.now().date():
				tl_list.append(TimelineItem(course.title, course.one_time_schedule.once_date, arr.content))
		else:
			for arr in course.arrangements.all():
				if arr.time >= datetime.now().date():
					tl_list.append(TimelineItem(course.title, arr.time, arr.content))
	#tl_list.sort(key=operator.attrgetter('date'))

	today = []
	tomorrow = []
	later = []
	for item in tl_list:
		if item.date == datetime.now().date():
			today.append(item)
		elif item.date == datetime.now().date() + timedelta(days=1):
			tomorrow.append(item)
		else:
			later.append(item) 

	later.sort(key=operator.attrgetter('date'))
	return today, tomorrow, later

@login_required
def schedule(request):
	user = request.user
	today, tomorrow, later = find(user)
	
	return render(request, 
			'schedule/timeline.html', 
			{'today':today, 'tomorrow':tomorrow, 'later':later})
