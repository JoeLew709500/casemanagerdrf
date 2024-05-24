from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Incident(models.Model):
    """
    Model to record incidents
    """
    location = models.CharField(max_length=200)
    incident_category = models.CharField(max_length=200)
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
