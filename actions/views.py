from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Action, ActionPhoto
from .serializers import ActionPhotoSerializer, ActionSerializer


# Create your views here.
class ActionCreateView(generics.CreateAPIView):
    """
    View to create an action
    """

    serializer_class = ActionSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActionListView(generics.ListCreateAPIView):
    """
    View to list and create actions
    """

    serializer_class = ActionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Action.objects.filter(created_by=self.request.user, incident_id=self.kwargs['pk'])

class ActionDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update and delete an action
    """

    serializer_class = ActionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Action.objects.filter(created_by=self.request.user)
    
    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            return print(serializer.errors)

class ActionDeleteView(generics.DestroyAPIView):
    """
    View to delete an action
    """

    serializer_class = ActionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Action.objects.filter(created_by=self.request.user)
    
    def perform_destroy(self, instance):
        instance.delete()

class ActionPhotoListView(generics.ListCreateAPIView):
    """
    View to list and create action photos
    """

    serializer_class = ActionPhotoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ActionPhoto.objects.filter(action_id__created_by=self.request.user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            return print(serializer.errors)
        
class ActionPhotoDeleteView(generics.DestroyAPIView):
    """
    View to delete an action photo
    """

    serializer_class = ActionPhotoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ActionPhoto.objects.filter(action_id__created_by=self.request.user)
    
    def perform_destroy(self, instance):
        instance.delete()
