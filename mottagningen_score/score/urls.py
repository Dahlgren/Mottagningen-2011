from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Piston
from piston.resource import Resource

# Piston handlers
from score.api.handlers import *
from score.api.mobile import *

urlpatterns = patterns('',
    # Frontend
    url(r'^admin/', 'score.views.admin'),
    url(r'^demo/', 'score.views.demo'),
    url(r'^graph/', 'score.views.graph'),
    
    # Frontend API
    url(r'^day/$', Resource(handler=ScoreHandler)),
    #url(r'^day/(?P<date>[^/]+)/$', Resource(handler=ScoreHandler)), // Obsolete
    url(r'^group/(?P<id>[^/]+)/$', Resource(handler=GroupHandler)),
    
    # Mobile API
    url(r'^groups', Resource(handler=GroupsHandler)),
    url(r'^post', Resource(handler=PostScoreHandler)),
    url(r'^days', Resource(handler=DaysHandler))
)

urlpatterns += staticfiles_urlpatterns()