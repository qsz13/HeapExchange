from django.contrib import admin
from post.models import Tag, Course, Activity, OneTimeSchedule


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    pass


@admin.register(OneTimeSchedule)
class OneTimeScheduleAdmin(admin.ModelAdmin):
    pass
