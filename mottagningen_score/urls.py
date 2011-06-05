from django.conf.urls.defaults import patterns, include, url

# Piston
from piston.resource import Resource

# Piston handlers
from mottagningen_django.score.handlers import *

urlpatterns = patterns('',
    # Get all devices
    url(r'^day/(?P<nr>[^/]+)/$', Resource(handler=ScoreHandler)),
    url(r'^groups/', Resource(handler=GroupsHandler)),
    url(r'^post', Resource(handler=PostScoreHandler))
)