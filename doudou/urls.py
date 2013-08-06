from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'doudou.views.home', name='home'),
    # url(r'^doudou/', include('doudou.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),'
    url(r'^$', 'doudou.views.index'),
    url(r'^index/', 'doudou.views.index'),
    url(r'^contacts/', 'doudou.views.contacts'),
    url(r'^login/', 'blog.views.user_login'),
    url(r'^logout/', 'blog.views.user_logout'),
    url(r'^registe/', 'blog.views.regist'),
    url(r'^blog/', include('blog.urls')),
)
