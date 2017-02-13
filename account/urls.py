from __future__ import unicode_literals
from django.conf.urls import url
from account import views

urlpatterns = [
    url("^profile/(?P<username>.*$)", view=views.profile, name='profile'),
    url("^profile/", view=views.profile, name='user_profile'),
	url("^subcription/", view=views.subcription, name='subcription'),
]