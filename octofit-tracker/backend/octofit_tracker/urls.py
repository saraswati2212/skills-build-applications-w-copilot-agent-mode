"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .views import TeamViewSet, ActivityViewSet, LeaderboardViewSet, WorkoutViewSet

router = DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboard', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)

import os
@api_view(['GET'])
def api_root(request, format=None):
    cs_name = os.environ.get('CODESPACE_NAME')
    if cs_name:
        # Use HTTPS for Codespaces public URL to avoid certificate issues
        base = f"https://{cs_name}-8000.app.github.dev/api/"
    else:
        # Use HTTP for localhost
        base = request.build_absolute_uri('/api/')
    return Response({
        'teams': base + 'teams/',
        'activities': base + 'activities/',
        'leaderboard': base + 'leaderboard/',
        'workouts': base + 'workouts/',
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', api_root, name='api-root'),
    path('', api_root, name='api-root'),
]
