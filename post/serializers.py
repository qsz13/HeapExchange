from rest_framework import serializers
from post.models import Course

__author__ = 'danielqiu'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'time', 'description', 'requirement', 'location')


