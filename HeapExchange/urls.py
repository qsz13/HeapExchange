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
    url(r'^post/', include('post.urls')),
    url(r'^heap_admin/', include('heap_admin.urls')),
    url(r'^announcement/', include('announcement.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^heap_coin/', include('coin.urls')),


]
