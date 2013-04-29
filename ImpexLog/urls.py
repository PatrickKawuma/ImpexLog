from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from logistics.views import login_user, send_notification, display_carrierlocalization
from contactUs.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ImpexLog.views.home', name='home'),
    # url(r'^ImpexLog/', include('ImpexLog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^index/$', TemplateView.as_view(template_name = 'index.html')),
    
    url(r'^accounts/', include('registration.urls')),

    url(r'^loginuser/$', login_user),
    url(r'^carrierlocalization/$', display_carrierlocalization),
    url(r'^testing/$', send_notification),
    url("", include('django_socketio.urls')),
    url(r'^contactus/$', TemplateView.as_view(template_name = 'contactUs.html')),
    #url(r'^contact/$', contact),
    url(r'^accounts/profile/$', TemplateView.as_view(template_name = 'carrierlocalization.html')),
    
)
