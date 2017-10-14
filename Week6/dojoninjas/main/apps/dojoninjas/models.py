from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dojos(models.Model):
      dojoname = models.CharField(max_length=255)
      dojocity = models.TextField()
      dojostate =models.TextField()
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
class Ninjas(models.Model):
      ninja_firstname = models.CharField(max_length=255)
      ninja_lastname = models.CharField(max_length=255)
      dojo = models.ForeignKey(Dojos, related_name="ninjas")

      