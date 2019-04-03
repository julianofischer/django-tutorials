from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Extending the existing User model
class Professor(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     disciplina = models.CharField(max_length=100)
