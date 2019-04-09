from django.db import models

# Create your models here.
class Documento(models.Model):
    titulo = models.TextField()
    upload = models.FileField(upload_to='uploads/')
