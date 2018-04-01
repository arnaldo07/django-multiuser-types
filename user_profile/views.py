import account.views

from .forms import *
from .models import *
class SignupView(account.views.SignupView):

   form_class = SignupForm

   def after_signup(self, form):
       self.create_profile(form)
       super(SignupView, self).after_signup(form)

   def create_profile(self, form):
   		profile = UserProfile()
   		profile.user = self.created_user  # replace with your reverse one-to-one profile attribut
   		profile.location= form.cleaned_data["location"]
   		profile.is_student = True
   		profile.save()