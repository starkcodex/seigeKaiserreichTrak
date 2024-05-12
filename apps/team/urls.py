from django.urls import path, include
from . import views

app_name = 'team'

urlpatterns = [
    path('myaccount/teams/add/', views.add, name='add'),
    path('activate_team/<int:team_id>/', views.activate_team, name='activate_team'),
    path('<int:team_id>/', views.team, name='team'),
    path('edit/', views.edit, name='edit'),
]
