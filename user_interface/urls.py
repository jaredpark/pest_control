from django.conf.urls import patterns, url
from user_interface import views

urlpatterns = patterns('',
    url(r'^account', views.account, name = 'account'),
    url(r'^register', views.register, name = 'register'),
    url(r'^login', views.myLogin, name = 'login'),
    url(r'^logout', views.logout, name = 'logout'),
)