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

    class Meta:
        model = Action
        fields = ['id', 'incident', 'created_on', 'created_by', 'action_code',
                  'details', 'completed_on']
        extra_kwargs = {
            'created_by': {'read_only': True},
        }