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

# class CustomerList(APIView):
#   def get(self, request, format=None):
#     customers = Customer.objects.all()
#     serializer = CustomerSerializer(customers, many=True)
#     return Response(serializer.data)

#   def post(self, request, format=None):
#     serializer = CustomerSerializer(data=request.DATA)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CustomerDetails(APIView):

#   def get_object(self, id):
#     try:
#       return Customer.objects.get(id=id)
#     except Customer.DoesNotExist:
#       raise Http404

#   def get(self, request, id, format=None):
#     customer = self.get_object(id)
#     serializer = CustomerSerializer(customer)
#     return Response(serializer.data)
  
#   def put(self, request, id, format=None):
#     customer = self.get_object(id)
#     serializer = CustomerSerializer(customer, data=request.DATA)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#     return Response(status=status.HTTP_400_BAD_REQUEST)
  
#   def delete(self, request, id, format=None):
#     customer = self.get_object(id)
#     customer.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)