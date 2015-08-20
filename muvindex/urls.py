"""muvindex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from movies.views import (index, movie_detail, actor_detail,
                          register_user, login_user, logout_user)

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^movies/(?P<movie_id>[0-9]+)/$', movie_detail, name='mov_detail'),
    url(r'^actors/(?P<actor_id>[0-9]+)/$', actor_detail, name='act_detail'),
    url(r'^register$', register_user, name='register'),
    url(r'^login', login_user, name='login'),
    url(r'^logout', logout_user, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
]
