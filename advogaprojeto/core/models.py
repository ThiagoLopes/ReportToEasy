from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):

    nome = models.CharField(max_length=50, null= False, unique=True)
    telefone = models.CharField(max_length=12, null= False)
    email = models.CharField(max_length=30, null=False, unique=True)
    user = models.OneToOneField(User, related_name="Usuario")

class Template(models.Model):

    texto = models.TextField(max_length=500, null=False)