from .models import Course, Activity, Arrangement

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