"""
URL configuration for casemanagerdrf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from authusers.views import CreateUserView, UserDetailView, UserListView
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("authusers/create/", CreateUserView.as_view(), name="create_user"),
    path("authusers/list/", UserListView.as_view(), name="list_users"),
    path("authusers/<int:pk>/", UserDetailView.as_view(), name="user_details"),
    path("authusers/token/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("authusers/token/refresh/",
         TokenRefreshView.as_view(), name="token_refresh"),
    path("authusers-api/", include("rest_framework.urls")),
    path("incident/", include("incident.urls")),
    path("actions/", include("actions.urls")),
]
