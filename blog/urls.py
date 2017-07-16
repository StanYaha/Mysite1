from django.conf.urls import include, url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'
     r'(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share')
]
