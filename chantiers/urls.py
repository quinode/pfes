from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('chantiers.views',
    (r'^$', 'index'),
    (r'^(?P<cslug>[-\w]+)/$', 'detail'),
)
