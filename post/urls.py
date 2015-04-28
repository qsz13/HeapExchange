from django.conf.urls import patterns, url
from post import views

urlpatterns = [
                       url(r'^$', views.all_course, name='post'),
                       url(r'all_tags', views.all_tags, name='all_tags'),
                       url(r'^course/create/$', views.get_course_form, name='course_create'), 
                       url(r'^course/posted/$', views.posted_course, name='posted_course'), 
                       url(r'^course/all/$', views.all_course, name='all_course'),
                       url(r'^course/joined/$', views.joined_course, name='joined_course'),
                       url(r'^course/interested/$', views.interested_course, name='interested_course'),
                       url(r'^course/(?P<course_id>[0-9]+)/$', views.course_detail, name='course_detail'),
                       url(r'^course/join/(?P<course_id>[0-9]+)/$', views.join_course, name='join_course'), 
                       url(r'^course/unjoin/(?P<course_id>[0-9]+)/$', views.unjoin_course, name='unjoin_course'), 
                       url(r'^course/interest/(?P<course_id>[0-9]+)/$', views.interest_course, name='interest_course'), 
                       url(r'^course/uninterest/(?P<course_id>[0-9]+)/$', views.uninterest_course, name='uninterest_course'),
                       url(r'^course/explore_list/', views.CourseExploreList.as_view(), name='course_explore_list_api')
                       #url(r'^course/interestin/$', views.interest_in_course, name='interest_in_course'),
                       # url(r'^login/$', views.LoginView.as_view(), name='login'),
                       # url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout', kwargs={'next_page': '/'}),
                       # url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
                       # url(r'^setting/$', views.SettingView.as_view(), name='setting'),
                       ]