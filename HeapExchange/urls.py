from django.conf.urls import include, url
from django.contrib import admin
from HeapExchange import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'HeapExchange.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.HomeView.as_view(), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls')),

]
