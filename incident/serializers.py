from rest_framework import serializers

from .models import Incident


class IncidentSerializer(serializers.ModelSerializer):
    """
    Serializer for Incident model
    """

    class Meta:
        model = Incident
        fields = ['id', 'location', 'incident_category', 'created_on',
                  'created_by', 'received_on', 'details', 'closed_on']
        extra_kwargs = {
            'created_by': {'read_only': True},
        }
