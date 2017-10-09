from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$',views.index),
    url(r'^create/$',views.create),
    url(r'^(?P<number>\d+)$',views.blog_post),
    url(r'^edit/(?P<number>\d+)$',views.blog_post_edit),
    url(r'^delete/(?P<number>\d+)$',views.destroy)
]