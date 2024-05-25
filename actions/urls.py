from django.urls import path

from . import views

urlpatterns = [
    path("list/<int:pk>/", views.ActionListView.as_view(), name="action_list"),
    path("<int:pk>/", views.ActionDetailView.as_view(),
         name="action_delete"),
    path("create/", views.ActionCreateView.as_view()),
    path("delete/<int:pk>/", views.ActionDeleteView.as_view()),
]