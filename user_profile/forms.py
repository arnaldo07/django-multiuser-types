
from django import forms

import account.forms


class SignupForm(account.forms.SignupForm):

    location = forms.CharField(max_length=100)