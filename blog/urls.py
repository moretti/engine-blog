from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from blog import views

urlpatterns = patterns(
    '',
    url(r'^$',
        views.PostList.as_view(), name='post_list'),
    url(r'^id/(?P<pk>\d+)$',
        views.PostDetail.as_view(), name='post_detail'),
    url(r'^new-post$',
        login_required(views.PostCreate.as_view()), name='post_new'),
    url(r'^edit-post/(?P<pk>\d+)$',
        login_required(views.PostUpdate.as_view()), name='post_edit'),
    url(r'^delete-post/(?P<pk>\d+)$',
        login_required(views.PostDelete.as_view()), name='post_delete'),
    url(r'^about$',
        TemplateView.as_view(template_name="about.html"), name='about'),
)
