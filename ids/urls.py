from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^honeypot/','ids.honeypot.views.index'),
    (r'^report/','ids.core.views.report'),
)
