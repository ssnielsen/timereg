from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from freelancr import views

urlpatterns = [
  url(r'^$', views.index),
  url(r'^customer/$', views.CustomerList.as_view()),
  url(r'^customer/(?P<id>[0-9]+)/$', views.CustomerDetails.as_view()),
  url(r'^customer/(?P<id>[0-9]+)/projects/$', views.CustomerProjects.as_view()),
  url(r'^project/$', views.ProjectList.as_view()),
  url(r'^project/(?P<id>[0-9]+)/$', views.ProjectDetails.as_view()),
  url(r'^activity/$', views.ActivityList.as_view()),
  url(r'^activity/(?P<id>[0-9]+)/$', views.ActivityDetails.as_view()),
  # url(r'^auth/register/$', views.register),
  # url(r'^auth/login/$', views.login_user),
  # url(r'^auth/logout/$', views.logout_user),
]

urlpatterns = format_suffix_patterns(urlpatterns)