from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cg4.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'main/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'main/logout.html'}),
    url(r'^pw_change/$', 'django.contrib.auth.views.password_change',
        {'template_name': 'main/pw_change.html'}, name="password_change"),
    url(r'^pw_change_done/$', 'django.contrib.auth.views.password_change_done',
        {'template_name': 'main/pw_change_done.html'}, name="password_change_done"),
    url(r'^create_teacher/$', 'create_teacher.views.create_teacher'),
)
