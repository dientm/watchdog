from __future__ import unicode_literals
from django.conf.urls import url
from webapp import views

urlpatterns = [
    url('/login$', view=views.login, name='login'),
]