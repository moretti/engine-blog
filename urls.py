from django.conf.urls.defaults import url, patterns, include
import dbindexer

handler500 = 'djangotoolbox.errorviews.server_error'

# search for dbindexes.py in all INSTALLED_APPS and load them
dbindexer.autodiscover()

urlpatterns = patterns(
    '',
    url('^_ah/warmup$', 'djangoappengine.views.warmup'),
    url('^$', 'django.views.generic.simple.direct_to_template',
        {'template': 'home.html'}),
    url(r'^accounts/login/$',
        'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$',
        'django.contrib.auth.views.logout'),
    url(r'^blog/', include('blog.urls')),
)
