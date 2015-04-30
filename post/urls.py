from django.conf.urls import patterns, url
from post import views

urlpatterns = [
                       url(r'^$', views.all_course, name='post'),

                       url(r'all_tags', views.all_tags, name='all_tags'),

                       url(r'^course/create/$', views.create_course, name='create_course'), 
                       url(r'^activity/create/$', views.create_activity, name='create_activity'), 

                       url(r'^course/posted/$', views.posted_course, name='posted_course'), 
                       url(r'^activity/posted/$', views.posted_activity, name='posted_activity'), 
                       
                       url(r'^course/all/$', views.all_course, name='all_course'),
                       url(r'^activity/all/$', views.all_activity, name='all_activity'),

                       url(r'^course/joined/$', views.joined_course, name='joined_course'),
                       url(r'^activity/joined/$', views.joined_activity, name='joined_activity'),

                       url(r'^course/interested/$', views.interested_course, name='interested_course'),
                       url(r'^activity/interested/$', views.interested_activity, name='interested_activity'),
                       
                       url(r'^course/(?P<course_id>[0-9]+)/$', views.course_detail, name='course_detail'),
                       url(r'^activity/(?P<activity_id>[0-9]+)/$', views.activity_detail, name='activity_detail'),

                       url(r'^course/join/(?P<course_id>[0-9]+)/$', views.join_course, name='join_course'), 
                       url(r'^course/unjoin/(?P<course_id>[0-9]+)/$', views.unjoin_course, name='unjoin_course'), 
                       url(r'^course/interest/(?P<course_id>[0-9]+)/$', views.interest_course, name='interest_course'), 
                       url(r'^course/uninterest/(?P<course_id>[0-9]+)/$', views.uninterest_course, name='uninterest_course'),

                       url(r'^activity/join/(?P<activity_id>[0-9]+)/$', views.join_activity, name='join_activity'), 
                       url(r'^activity/unjoin/(?P<activity_id>[0-9]+)/$', views.unjoin_activity, name='unjoin_activity'), 
                       url(r'^activity/interest/(?P<activity_id>[0-9]+)/$', views.interest_activity, name='interest_activity'), 
                       url(r'^activity/uninterest/(?P<activity_id>[0-9]+)/$', views.uninterest_activity, name='uninterest_activity'),


                       url(r'^course/explore_list/', views.CourseExploreList.as_view(), name='course_explore_list_api'),
                       
                       url(r'^course/update/(?P<course_id>[0-9]+)/$', views.update_course, name='update_course'),
                       url(r'^activity/update/(?P<activity_id>[0-9]+)/$', views.update_activity, name='update_activity'),

                       url(r'^course/remove/(?P<course_id>[0-9]+)/$', views.remove_course, name='remove_course'), 
                       url(r'^activity/remove/(?P<activity_id>[0-9]+)/$', views.remove_activity, name='remove_activity'), 

                       url(r'^course/addtag/(?P<course_id>[0-9]+)/$', views.course_add_tag, name='course_add_tag'),
                       
                       #url(r'^course/interestin/$', views.interest_in_course, name='interest_in_course'),
                       # url(r'^login/$', views.LoginView.as_view(), name='login'),
                       # url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout', kwargs={'next_page': '/'}),
                       # url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
                       # url(r'^setting/$', views.SettingView.as_view(), name='setting'),
                       ]