from django.conf.urls import patterns, include, url
from django.contrib import admin
from homepage import views

from user_interface.forms import MyRegistrationForm, MyProfileForm
from registration.backends.default.views import RegistrationView

admin.autodiscover()

# class MyRegistrationView(RegistrationView):
#     def get_success_url(self,request, user):
#         return('/accounts/login/')

urlpatterns = patterns('',
    url(r'^$', include('homepage.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/', include('contact.urls')),
	# url(r'^my_account/', include('user_interface.urls')),
    url(r'accounts/register/$', RegistrationView.as_view(form_class = MyRegistrationForm), name = 'registration_register'),
	url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^profiles/edit', 'myProfiles.views.edit_profile', {'form_class': MyProfileForm}),
    url(r'^profiles/home', 'myProfiles.views.home', name = 'profiles_home'),
    url(r'^profiles/', include('myProfiles.urls')),
	# url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
	url(r'^about/', views.about, name = 'about'),
    url(r'^products/', views.products, name = 'products'),
    url(r'^specials/', views.specials, name = 'specials'),
)
