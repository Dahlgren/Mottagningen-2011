from django.conf.urls.defaults import patterns, include, url

from oauth_provider.views import protected_resource_example

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mottagningen_django.views.home', name='home'),
    # url(r'^mottagningen_django/', include('mottagningen_django.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^score/', include('score.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^oauth/', include('oauth_provider.urls')),
    url(r'^oauth/photo/$', protected_resource_example, name='oauth_example')
)
