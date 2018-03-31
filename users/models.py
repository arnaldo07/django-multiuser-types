from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class User(AbstractUser):
	is_student = models.BooleanField(default=False)
	is_teacher = models.BooleanField(default=False)
	is_secretary = models.BooleanField(default=False)

class Account(AbstractUser):

	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete='CASCADE')
	def __str__(self):
		return str(self.user)
