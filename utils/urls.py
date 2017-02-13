from __future__ import unicode_literals
from future.builtins import str

from django.shortcuts import redirect

LOGIN_REDIRECT_URL = '/account/profile'

def login_redirect(request) :
	next = LOGIN_REDIRECT_URL
	redirect(next)