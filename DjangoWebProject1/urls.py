"""
Definition of urls for DjangoWebProject1.
"""
from django.conf.urls import url
from app.views import twitter, instagram
# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    
    url(r'^$', twitter, name='twitter'),
    url(r'^instagram', instagram, name='instagram')	,

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
