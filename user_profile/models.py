from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class UserProfile():
	location = models.CharField(max_length=100)
	is_student = models.BooleanField(default=False)
	is_teacher = models.BooleanField(default=False)
