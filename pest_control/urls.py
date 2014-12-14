from django.conf.urls import patterns, include, url
from django.contrib import admin
from homepage import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pest_control.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.homepage, name = 'homepage'),
)
