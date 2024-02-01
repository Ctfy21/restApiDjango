from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .models import Experiment
from .serializers import ExperimentSerializer

class ExperimentAPIList(generics.ListCreateAPIView):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer

class ExperimentAPIUpdate(generics.UpdateAPIView):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    
class ExperimentAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer