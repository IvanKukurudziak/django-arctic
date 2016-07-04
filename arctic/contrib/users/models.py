from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

class UserRole(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='role')
    role = models.ForeignKey('Role')

class Role(models.Model):
    name = models.CharField('Role', max_length=100)
    is_active = models.BooleanField(default=True)