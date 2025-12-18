from django.urls import path
from .views import *


urlpatterns = [
    path(
        '',
        HomeView.as_view(),
        name='home'
    ),
    path(
        'project/<int:project_id>/',
        ProjectsDetailView.as_view(),
        name='project_detail'
    ),
]