from django.urls import path

from . import views

urlpatterns = [
    path("list/<int:pk>/", views.ActionListView.as_view(), name="action_list"),
    path("<int:pk>/", views.ActionDetailView.as_view(),
         name="action_delete"),
    path("create/", views.ActionCreateView.as_view()),
    path("delete/<int:pk>/", views.ActionDeleteView.as_view()),
    path("photo/", views.ActionPhotoListView.as_view(), name="action_photo_create"),
    path("photo/delete/<int:pk>/", views.ActionPhotoDeleteView.as_view(), name="action_photo_delete"),
    path("photo/create/", views.ActionPhotoCreateView.as_view(), name="action_photo_create"),
]