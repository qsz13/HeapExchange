from django.conf.urls import patterns, url
from post import views

urlpatterns = [
                       url(r'^$', views.all_course, name='post'),
                       url(r'^course/create/$', views.get_course_form, name='course_create'), 
                       url(r'^course/posted/$', views.posted_course, name='posted_course'), 
                       url(r'^course/all/$', views.all_course, name='all_course'),
                       url(r'^course/join/(?P<course_id>[0-9]+)/$', views.join_course, name='join_course'), 
                       #url(r'^course/interestin/$', views.interest_in_course, name='interest_in_course'),
                       # url(r'^login/$', views.LoginView.as_view(), name='login'),
                       # url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout', kwargs={'next_page': '/'}),
                       # url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
                       # url(r'^setting/$', views.SettingView.as_view(), name='setting'),
                       ]