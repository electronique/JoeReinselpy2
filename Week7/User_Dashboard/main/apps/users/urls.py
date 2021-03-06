from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^show/(?P<id>\d+)$', views.show),
    url(r'^admin/edit/(?P<id>\d+)$', views.edit),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^admin/edit/processedit/(?P<id>\d+)$', views.processedit),
    url(r'^add/$', views.add),
    url(r'^new/$', views.new),
    url(r'^admin/$', views.admin),

]