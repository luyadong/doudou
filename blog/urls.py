from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'blog.views.index'),
    url(r'^write/$', 'blog.views.write'),
)
