from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .api import CreateUserAPI

urlpatterns = [
    path('register', CreateUserAPI.as_view(), name='register-user'),
    path('login', obtain_auth_token, name='login'),
    path('create-superuser', CreateUserAPI.as_view(), name='register-superuser'),
    path('create-staffuser', CreateUserAPI.as_view(), name='register-staffuser'),
]
