from django.conf.urls import url
from account import views

__author__ = 'danielqiu'

urlpatterns = [
                       url(r'^$', views.AccountView.as_view(), name='account'),
                       url(r'^signup/$', views.SignUpView.as_view(), name='sign_up'),
                       url(r'^login/$', views.LoginView.as_view(), name='login'),
                       url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout', kwargs={'next_page': '/'}),
                       # url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
                       # url(r'^setting/$', views.SettingView.as_view(), name='setting'),
                       ]