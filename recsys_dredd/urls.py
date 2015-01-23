# from django.conf.urls import patterns, include, url
# from django.contrib import admin

# urlpatterns = patterns('',
#     url(r'/', include('recsys_app.urls')),
# )

from django.conf.urls import patterns, url

from recsys_app import views

urlpatterns = patterns('',
    url(r'index.html', views.index),
)