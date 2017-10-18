from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Books(models.Model):
      title = models.CharField(max_length=255)
      description = models.TextField()
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
class Author(models.Model):
      firstname = models.CharField(max_length=255)
      lastname = models.CharField(max_length=255)
      booktitle = models.ForeignKey(Books, related_name="Author")