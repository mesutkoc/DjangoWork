from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^project/$',projectview, name='project'),
    url(r'^projectcreate/$',project_create,name='projectcreate'),
    url(r'^mainpage/$',mainpage, name='mainpage'),
    url(r'^(?P<id>\d+)/projectupdate/$',project_update),
    url(r'^(?P<id>\d+)/projectdelete/$',project_delete,name='projectdelete'),
    url(r'^(?P<id>\d+)/projectcompleted/$', project_completed, name='projectcompleted'),
    url(r'^(?P<id>\d+)/projectleave/$', project_leave, name='projectleave'),
    url(r'^(?P<id>\d+)/projectposts/$',project_posts,name='projectposts'),
    url(r'^postcreate/$',post_create,name='postcreate'),
    url(r'^(?P<id>\d+)/update/$', post_update),
    url(r'^(?P<id>\d+)/delete/$',post_delete,name='delete'),
    url(r'^addteammates/$',enroll_user,name='addteammates'),

]
