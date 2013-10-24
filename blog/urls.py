from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from blog import views

urlpatterns = patterns(
    '',
    url(r'^$',
        views.PostList.as_view(), name='post_list'),
    url(r'^new$',
        login_required(views.PostCreate.as_view()), name='post_new'),
    url(r'^edit/(?P<pk>\d+)$',
        login_required(views.PostUpdate.as_view()), name='post_edit'),
    url(r'^delete/(?P<pk>\d+)$',
        login_required(views.PostDelete.as_view()), name='post_delete'),
)
