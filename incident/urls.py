from django.urls import path

from . import views

urlpatterns = [
    path("", views.IncidentListView.as_view(), name="incident_list"),
    path("<int:pk>/", views.IncidentDeleteView.as_view(),
         name="incident_delete"),
]
