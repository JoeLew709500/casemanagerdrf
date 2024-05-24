from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Incident
from .serializers import IncidentSerializer


# Create your views here.
class IncidentListView(generics.ListAPIView):
    """
    View to list all incidents
    """

    serializer_class = IncidentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Incident.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(created_by=self.request.user)
        else:
            return print(serializer.errors)
        
class IncidentDeleteView(generics.DestroyAPIView):
    """
    View to delete an incident
    """

    serializer_class = IncidentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Incident.objects.filter(created_by=self.request.user)
    
    def perform_destroy(self, instance):
        instance.delete()

class IncidentCreateView(generics.CreateAPIView):
    """
    View to create an incident
    """

    serializer_class = IncidentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(created_by=self.request.user)
        else:
            return print(serializer.errors)
