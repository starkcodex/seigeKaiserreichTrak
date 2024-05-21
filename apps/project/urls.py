from django.urls import path
from . import views

app_name = 'project'


urlpatterns = [
    path('projects/', views.projects, name='projects'),
    path('<int:project_id>/', views.project, name='project'),
]
