from rest_framework import serializers
from freelancr.models import Activity, Customer, Project

class ActivitySerializer(serializers.ModelSerializer):
  date = serializers.DateField(format='iso-8601')
  class Meta:
    model = Activity
    fields = ('id', 'project', 'duration', 'date', 'description', 'rate', 'billed', 'payed')

class ProjectSerializer(serializers.ModelSerializer):
  activities = ActivitySerializer(many=True, required=False)

  class Meta:
    model = Project
    fields = ('id', 'customer', 'name', 'activities')

class CustomerSerializer(serializers.ModelSerializer):
  projects = ProjectSerializer(many=True, required=False)

  class Meta:
    model = Customer
    fields = ('id', 'name', 'street', 'phone', 'projects')

