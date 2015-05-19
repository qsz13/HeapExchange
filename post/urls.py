from django.conf.urls import patterns, url
from post import views

urlpatterns = [
                       url(r'^$', views.all_post, name='post'),

                       # create course & activity
                       url(r'^create/(?P<kind>a|c)/$', views.create, name='create'),
                       
                       # all posts
                       url(r'^all/(?P<kind>[a,c]{1})/$', views.all_post, name='all'),
                       
                       # posted posts
                       url(r'^posted/(?P<kind>[a,c]{1})/$', views.posted, name='posted'),
                       
                       # joined posts
                       url(r'^joined/(?P<kind>[a,c]{1})/$', views.joined, name='joined'),
                       
                       # interested posts
                       url(r'^interested/(?P<kind>[a,c]{1})/$', views.interested, name='interested'),
                       
                       # post detail
                       url(r'^detail/(?P<kind>a|c)/(?P<post_id>[0-9]+)/$', views.detail, name='detail'),

                       # edit arrangement
                       url(r'^arrange/edit/(?P<post_id>[0-9]+)/$', views.edit_arrange, name='edit_arrange'),
                       
                       # post actions
                       url(r'^join/(?P<kind>[a,c]{1})/(?P<post_id>[0-9]+)/$', views.join, name='join'),
                       url(r'^unjoin/(?P<kind>[a,c]{1})/(?P<post_id>[0-9]+)/$', views.unjoin, name='unjoin'),
                       url(r'^interest/(?P<kind>[a,c]{1})/(?P<post_id>[0-9]+)/$', views.interest, name='interest'),
                       url(r'^uninterest/(?P<kind>[a,c]{1})/(?P<post_id>[0-9]+)/$', views.uninterest, name='uninterest'),

                       url(r'^course/explore_list/', views.CourseExploreList.as_view(), name='course_explore_list_api'),
                       
                       # update post
                       url(r'^update/(?P<kind>[a,c]{1})/(?P<post_id>[0-9]+)/$', views.update, name='update'),
                       
                       # remove post
                       url(r'^remove/(?P<kind>[a,c]{1})/(?P<post_id>[0-9]+)/$', views.remove, name='remove'),
                       
                       # tag
                       url(r'^addtag/(?P<kind>[a,c]{1})/(?P<post_id>[0-9]+)/$', views.add_tag, name='addtag'),
                       
                       url(r'^all_tags/$', views.all_tags, name='all_tags'),
                       url(r'^tagview/(?P<tag_id>[0-9]+)/$', views.tag_view, name='tagview'),
                       
                       ]
