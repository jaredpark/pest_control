from django.conf.urls import patterns, url

from myProfiles import views

urlpatterns = patterns('',
  # url(r'^create/$',
    # views.create_profile,
    # name='profiles_create_profile'),
  url(r'^edit/$',
    views.edit_profile,
    name='profiles_edit_profile'),
  url(r'^(?P<username>\w+)/$',
    views.profile_detail,
    name='profiles_profile_detail'),
  # url(r'^$',
  #   views.profile_list,
  #   name='profiles_profile_list'),
)
