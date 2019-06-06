from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile/(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
    url(r'^bunk', views.bunk, name='bunk'),
    url(r'^logout', views.logout, name='bunk-logout'),
]
