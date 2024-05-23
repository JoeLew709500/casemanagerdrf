from django.contrib.auth.models import User
from django.db import models

# Create your models here.

INCIDENT_CATEGORY_CHOICES = (
    (1, 'Fly Tipping'),
    (2, 'Noise Pollution'),
    (3, 'Abandoned Vehicle'),
    (4, 'Littering'),
    (5, 'Statutory Nuisance (e.g. odour, light, etc.)'),
    (6, 'Presentation of Waste (Domestic)'),
    (7, 'Presentation of Waste (Commercial)'),
    (8, 'Atmospheric Pollution (e.g. smoke, fumes, etc.)'),
    (9, 'Accumulation of Waste'),
    (10, 'Trade Waste Checking'),
    (11, 'ASB (Anti-Social Behaviour)'),
)


class Incident(models.Model):
    """
    Model to record incidents
    """
    location = models.CharField(max_length=200)
    incident_category = models.IntegerField(choices=INCIDENT_CATEGORY_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='incidents')
    received_on = models.DateTimeField()
    details = models.TextField()
    closed_on = models.DateTimeField(null=True, blank=True)

    class Meta:
        """
        Meta class to order incidents by created_on
        """
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.get_incident_category_display()} - {self.location}"
