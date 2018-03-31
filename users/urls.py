
# Create your views here.
from django.conf.urls import include, url

from .views import *

urlpatterns = [
    url('accounts/signup/student/', StudentSignUpView.as_view(), name='student_signup'),
    url('accounts/signup/teacher/', TeacherSignUpView.as_view(), name='teacher_signup'),
    url('accounts/signup/secretary/', TeacherSignUpView.as_view(), name='secretary_signup'),
]