from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from .forms import *
from .models import User
# Create your views here.
def home(request):

	return ''


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = ''

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('')

class SecretarySignUpView(CreateView):
    model = User
    form_class = SecretarySignUpForm
    template_name = 'signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'secretary'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('')
