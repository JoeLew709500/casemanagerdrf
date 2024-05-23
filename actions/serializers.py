from rest_framework import serializers

from .models import Action, ActionPhoto


class ActionPhotoSerializer(serializers.ModelSerializer):
    """
    Serializer for ActionPhoto model
    """
    class Meta:
        model = ActionPhoto
        fields = ['id', 'photo', 'action_id']

class ActionSerializer(serializers.ModelSerializer):
    """
    Serializer for Action model
    """
    photos = ActionPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Action
        fields = ['id', 'incident', 'created_on', 'created_by', 'action_code',
                  'details', 'completed', 'completed_on']
        extra_kwargs = {
            'created_by': {'read_only': True},
        }