from django.urls import path
from django.conf import settings
from .views import home

urlpatterns = [
    path('', home, name='home'),
]

