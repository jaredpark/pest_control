from django.conf.urls import patterns, include, url
from django.contrib import admin
from homepage import views

urlpatterns = patterns('',
    url(r'^$', include('homepage.urls')),
    url(r'^myAdminPortal/', include(admin.site.urls)),
    url(r'^contact/', include('contact.urls')),
    url(r'^accounts/', include('user_interface.urls')),
    url(r'^about/', views.about, name = 'about'),
    url(r'^products/', views.products, name = 'products'),
    # url(r'^register/', views.register, name = 'register'),
    # url(r'^login/', views.myLogin, name = 'login'),
    # url(r'^logout/', views.user_logout, name = 'logout'),
    # url(r'^account/', views.account, name = 'account'),
)
