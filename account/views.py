from __future__ import unicode_literals
from future.builtins import str
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.contrib.messages import info, error
from django.contrib.auth import (login as auth_login)
from django.template.response import TemplateResponse

from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm
from django.contrib.auth.models import User

def home(request):
    # return HttpResponse("Hello world")
    return render(request, 'user/index.html')


def login(request, template="login.html"):
    form = LoginForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print 1
        authenticated_user = form.save()
        auth_login(request, authenticated_user)
        return redirect('/account/profile')
        # form = LoginForm(request.POST)
        # if form.is_valid():
            # authenticated_user = form.save()
            # info(request, _("Successfully logged in"))
            # auth_login(request, authenticated_user)
            # print 2
            # return redirect('/account/profile')
        # else:
        #     print form
    else:
        print form
    form = LoginForm()
    return render(request, template, {'form': form})

@login_required
def profile(request, username, template="account/account_profile.html",
            extra_context=None):
    """
    Display a profile
    """
    if username == '' or username is None:
        username = request.user.username
    lookup = {"username__iexact": username, "is_active": True}
    context = {"profile_user": get_object_or_404(User, **lookup)}
    context.update(extra_context or {})
    return TemplateResponse(request, template, context)



def subcription(request, template="account/subcription.html"):
    
    return render(request, template)