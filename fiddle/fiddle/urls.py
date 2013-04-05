from django.conf.urls.defaults import *
#django tastypie play

from formpost.api import PostResource

post_resource = PostResource()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    
    #url(r'^formpost/$', views.uPostlist.as_view()),
    # url(r'^formpost/(?P<pk>[0-9]+)/$',views.uPostDetail.as_view()),	
    # Examples:
    # url(r'^$', 'formpost.views.feedline', name='feedflow'),
    # url(r'^fiddle/', include('fiddle.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
    # url(r'^feedline',"formpost.views.feedline"),
    # url(r'^feedpost/',"formpost.views.feedPost"),                  
     url(r'^api/',include(post_resource.urls)),

)



