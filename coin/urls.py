from django.conf.urls import url
from coin import views

__author__ = 'danielqiu'
urlpatterns = [
                       url(r'^$', views.CoinView.as_view(), name='coin'),
                       url(r'^history/$', views.TransactionView.as_view(), name="transaction_history"),
                       url(r'^input/$', views.InputTransactionView.as_view(), name="input_transaction"),
                       url(r'^output/$', views.OutputTransactionView.as_view(), name="output_transaction"),
                       # url(r'^login/$', views.LoginView.as_view(), name='login'),
                       # url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout', kwargs={'next_page': '/'}),
                       # url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
                       # url(r'^setting/$', views.SettingView.as_view(), name='setting'),
                       ]