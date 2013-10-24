from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns(
    '',
    url(r'^$', views.PostList.as_view(), name='post_list'),
    url(r'^new$', views.PostCreate.as_view(), name='post_new'),
    url(r'^edit/(?P<pk>\d+)$',
        views.PostUpdate.as_view(), name='post_edit'),
    url(r'^delete/(?P<pk>\d+)$',
        views.PostDelete.as_view(), name='post_delete'),
)
