from django.conf.urls import patterns, include, url
from django.contrib import admin
from homepage import views

admin.autodiscover()

from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return('/accounts/login/')

urlpatterns = patterns('',
    url(r'^$', include('homepage.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/', include('contact.urls')),
	url(r'^my_account/', include('user_interface.urls')),
	url(r'^accounts/', include('registration.urls')),
	url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
	url(r'^about/', views.about, name = 'about'),
    url(r'^products/', views.products, name = 'products'),
    url(r'^specials/', views.specials, name = 'specials'),
)
