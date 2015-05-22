from django.conf.urls import patterns, url
from . import views

urlpatterns = [
	url(r'^(?P<kind>teach|join)/$', views.schedule, name='schedule'),
]