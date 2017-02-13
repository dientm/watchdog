from __future__ import unicode_literals
from django.conf.urls import url
from user import views

urlpatterns = [
    url('^$', view=views.edit_profile, name='edit_profile'),

]