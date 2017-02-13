from __future__ import unicode_literals
from django.contrib.auth import authenticate, get_user_model

from django import forms

from django.utils.translation import ugettext, ugettext_lazy as _


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput(render_value=False))

    def clean(self):
        """
        Authenticate the given username/email and passowrd. If the fields
        are valid, store the authenticated user for returning via save().
        :return:
        """
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        self._user = authenticate(username=username, password=password)
        if self._user is None:
            raise forms.ValidationError(
                            ugettext("Invalid username/email and password"))
        elif not self._user.is_active:
            raise forms.ValidationError(
                ugettext("Your account is inactive")
            )
        return self.cleaned_data

    def save(self):
        """
        Just return the authenticated user - used for logging in.
        :return:
        """
        return getattr(self, "_user", None)