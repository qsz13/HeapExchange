from .models import Course, Activity, Arrangement
from notifications import notify

class DateJudge:
	def __init__(self, post):
		if post.schedule_type == 'ONCE':
			self.start_date = post.one_time_schedule.once_date
			self.end_date = post.one_time_schedule.once_date
		elif post.schedule_type == 'SEQU':
			self.start_date = post.sequence_time_schedule.sequence_start_date
			self.end_date = post.sequence_time_schedule.sequence_end_date
		else:
			self.start_date = post.weekly_time_schedule.weekly_start_date
			self.end_date = post.weekly_time_schedule.weekly_end_date


def noti(sender, post, content):
	receiver_list = post.joined.all()
	msg = '[' + post.title + '] ' + content
	for receiver in receiver_list:
		if receiver != sender:
			notify.send(sender, recipient=receiver, verb=msg)
	if post.initiator != sender:
		notify.send(sender, recipient=post.initiator, verb=msg)
