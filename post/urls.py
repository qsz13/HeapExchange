from django.conf.urls import patterns, url
from post import views

urlpatterns = [
                       url(r'^$', views.TempView.as_view(), name='post'),
                       url(r'^course/create', views.CourseCreateView.as_view(), name='course_create')
                       # url(r'^login/$', views.LoginView.as_view(), name='login'),
                       # url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout', kwargs={'next_page': '/'}),
                       # url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
                       # url(r'^setting/$', views.SettingView.as_view(), name='setting'),
                       ]