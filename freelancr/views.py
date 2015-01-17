from django.http import Http404
from django.shortcuts import render_to_response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from freelancr.models import Customer, Project, Activity
from freelancr.serializers import CustomerSerializer, ProjectSerializer, ActivitySerializer

def index(request):
  return render_to_response('freelancr/index.html')

class CustomerList(generics.ListCreateAPIView):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer

class CustomerDetails(generics.RetrieveUpdateDestroyAPIView):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer
  lookup_field = 'id'

class CustomerProjects(generics.ListAPIView):
  serializer_class = ProjectSerializer

  def get_queryset(self):
    projects = Project.objects.filter(customer=self.kwargs['id'])
    return projects

class ProjectList(generics.ListCreateAPIView):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer

class ProjectDetails(generics.RetrieveUpdateDestroyAPIView):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer
  lookup_field = 'id'

class ActivityList(generics.ListCreateAPIView):
  queryset = Activity.objects.all()
  serializer_class = ActivitySerializer

class ActivityDetails(generics.RetrieveUpdateDestroyAPIView):
  queryset = Activity.objects.all()
  serializer_class = ActivitySerializer
  lookup_field = 'id'

class ProjectActivities(generics.ListAPIView):
  serializer_class = ActivitySerializer

  def get_queryset(self):
    activities = Activity.objects.filter(project=self.kwargs['id'])
    return activities