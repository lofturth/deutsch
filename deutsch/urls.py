from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'quizzes.views.home', name='home'),
    url(r'^quiz/(?P<quiz_pk>\d*)$', 'quizzes.views.quiz', name='quiz'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login/'}),

)
