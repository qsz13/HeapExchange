from django.shortcuts import render
from django.contrib.auth.models import User
from post.models import Course, Activity, Arrangement
from django.contrib.auth.decorators import login_required
import operator
from datetime import datetime, date, timedelta
import calendar

class TimelineItem:
	def __init__(self, id, flag, title, date,  content):
		self.id = id
		self.flag = flag
		self.title = title
		self.date = date
		self.content = content


def find(user):
	tl_list = []
	for course in user.courses.all():
		if course.schedule_type == 'ONCE':
			if course.one_time_schedule.once_date >= datetime.now().date():
				tl_list.append(TimelineItem(course.id, 'c', course.title, course.one_time_schedule.once_date, arr.content))
		else:
			for arr in course.arrangements.all():
				if arr.time >= datetime.now().date():
					tl_list.append(TimelineItem(course.id, 'c', course.title, arr.time, arr.content))
	for course in user.joined_courses.all():
		if course.schedule_type == 'ONCE':
			if course.one_time_schedule.once_date >= datetime.now().date():
				tl_list.append(TimelineItem(course.id, 'c', course.title, course.one_time_schedule.once_date, arr.content))
		else:
			for arr in course.arrangements.all():
				if arr.time >= datetime.now().date():
					tl_list.append(TimelineItem(course.id, 'c', course.title, arr.time, arr.content))
	#tl_list.sort(key=operator.attrgetter('date'))

	today = []
	today_date = datetime.now().date()
	tomorrow = []
	tomorrow_date = today_date + timedelta(days=1)
	this_week = []
	week_line = datetime.now().date() + timedelta(days=6 - today_date.weekday())
	this_month = []
	month_date = today_date + timedelta(days=
		calendar.monthrange(datetime.now().year, datetime.now().month)[1] - today_date.day)
	later = []
	for item in tl_list:
		if item.date == today_date:
			today.append(item)
		elif item.date == tomorrow_date:
			tomorrow.append(item)
		elif item.date <= week_line:
			this_week.append(item)
		elif item.date <= month_date:
			this_month.append(item)
		else:
			later.append(item) 

	this_week.sort(key=operator.attrgetter('date'))
	this_month.sort(key=operator.attrgetter('date'))
	later.sort(key=operator.attrgetter('date'))
	return today, tomorrow, this_week, this_month, later

@login_required
def schedule(request):
	user = request.user
	today, tomorrow, week, month, later = find(user)
	
	return render(request, 
			'schedule/timeline.html', 
			{'today':today, 'tomorrow':tomorrow, 'week':week, 
			'month':month, 'later':later})
