from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
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

# def register(request):
#   if not request.method == 'POST':
#     return HttpResponse(status = 405)

#   username = request.POST['username']
#   password = request.POST['password']
#   user = User.objects.create(username, 'admin@' + username + '.com', password)
#   user.save()

#   authed = authenticate(username = username, password = password)
#   login(request, authed)

#   return HttpResponse()

# def login_user(request):
#   print(request.POST)

#   if not request.method == 'POST':
#     return HttpResponse(status = 405)

#   username = request.POST['username']
#   password = request.POST['password']

#   authed = authenticate(username = username, password = password)
#   login(request, authed)

#   return HttpResponse()

# def logout_user(request):
#   if not request.method == 'POST':
#     return HttpResponse(status = 405)

#   logout(request)

#   return HttpResponse()



