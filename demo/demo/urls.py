"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from app_demo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.login),
    url(r'^index$', views.login),
    url(r'^index1$', views.login1),
    url(r'^index2$', views.login2),
    url(r'^index/admin$', views.admin),
    url(r'^test$', views.test),
    url(r'^index/admin/createstu$', views.createstu),
    url(r'^index/admin/createteacher$', views.createteacher),
    url(r'^index/admin/createcourse$', views.createcourse),
    url(r'^index/admin/retrievestu$', views.retrievestu),
    url(r'^index/admin/retrieveteacher$', views.retrieveteacher),
    url(r'^index/admin/retrievecourse$', views.retrievecourse),
    url(r'^index/admin/updatestu$', views.updatestu),
    url(r'^index/admin/updateteacher$', views.updateteacher),
    url(r'^index/admin/updatecourse$', views.updatecourse),
    url(r'^index/admin/statistic$', views.stat),
    url(r'^index1/professor$', views.pro),
    url(r'^index1/professor/allscore$', views.allscore),
    url(r'^index2/student$', views.stu),
]
