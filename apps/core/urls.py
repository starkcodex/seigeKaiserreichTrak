from django.urls import path, include
from . import views

apps = 'apps.core'

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('plans/', views.plans, name='plans'),
    path('signup/', views.signup, name='signup'),
]


