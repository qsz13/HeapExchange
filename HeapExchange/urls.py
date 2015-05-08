from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
import notifications
from HeapExchange import views
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'HeapExchange.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.HomeView.as_view(), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls')),
    url(r'^post/', include('post.urls', namespace='post', app_name='post')),
    url(r'^heap_admin/', include('heap_admin.urls')),
    url(r'^announcement/', include('announcement.urls')),
    url(r'^search/', include('search.urls', namespace='search', app_name='search')),
    url(r'^heap_coin/', include('coin.urls')),
    url(r'^message/', include('postman.urls')),
    url('^notifications/', include('notifications.urls', namespace='notifications')),
    url(r'^comments/', include('django_comments.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

