from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

apps = 'apps.core'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login', http_method_names = ['get', 'post', 'options']), name='logout'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('myaccount/edit_profile/', views.edit_profile, name='edit_profile'),
]


