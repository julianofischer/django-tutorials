from django.urls import path
from . import views

urlpatterns = [
    path("professorregister/", views.professor_register, name='professor_register'),
    path("professorregister2/", views.professor_register2, name='professor_register2'),
]
