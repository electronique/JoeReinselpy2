from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors["first_name"] = "User name should be more than 5 characters"
        if len(postData['last_name']) < 5:
            errors["last_name"] = "should be more than 10 characters"
        if len(postData['email']) < 5:
                errors["email"] = "User name should be more than 5 characters"
        if len(postData['password']) < 3:
            errors["password"] = "should be more than 10 characters"
        return errors;
class User(models.Model):
      first_name = models.CharField(max_length=255)
      last_name = models.CharField(max_length=255)
      email = models.CharField(max_length=255)
      password = models.CharField(max_length=255)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      objects = UserManager()