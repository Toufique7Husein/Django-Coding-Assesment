from .views import RegisterAPI
from django.urls import path

urlpatterns = [
    path('api/register/tfq', RegisterAPI.as_view(), name='register'),
]