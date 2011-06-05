from django.conf.urls.defaults import patterns, include, url

# Piston
from piston.resource import Resource

# Piston handlers
from score.handlers import *

urlpatterns = patterns('',
    url(r'^admin/', 'score.views.admin'),
    url(r'^day/$', Resource(handler=ScoreHandler)),
    url(r'^day/(?P<id>[^/]+)/$', Resource(handler=ScoreHandler)),
    url(r'^groups', Resource(handler=GroupsHandler)),
    url(r'^post', Resource(handler=PostScoreHandler)),
    url(r'^days', Resource(handler=DaysHandler))
)