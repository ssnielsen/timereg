from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
  name = models.CharField(max_length=255)
  street = models.CharField(max_length=255, default='N/A')
  phone = models.CharField(max_length=20, default='N/A')

  def __unicode__(self):
    return '{0} - {1}'.format(self.name, self.phone)

class Project(models.Model):
  customer = models.ForeignKey(Customer, related_name='projects')
  name = models.CharField(max_length=255)
  owner = models.ForeignKey(User, default=-1)

  def __unicode__(self):
    return '{0} - {1}'.format(self.customer.name, self.name)

class Activity(models.Model):
  project = models.ForeignKey(Project, related_name='activities')
  duration = models.FloatField()
  date = models.DateField(default=date.today())
  description = models.CharField(max_length=255)
  rate = models.IntegerField()
  billed = models.BooleanField(default=False)
  payed = models.BooleanField(default=False)