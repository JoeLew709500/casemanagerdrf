from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

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


class IncidentCreateView(generics.CreateAPIView):
    """
    View to create an incident
    """

    serializer_class = IncidentSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IncidentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update and delete an incident
    """

    serializer_class = IncidentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Incident.objects.filter(created_by=self.request.user)

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
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
