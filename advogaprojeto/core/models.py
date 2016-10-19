from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):

    nome = models.CharField(max_length=50, null= False)
    telefone = models.CharField(max_length=10, null= False)
    email = models.CharField(max_length=30, null=False)
    user = models.OneToOneField(User, related_name="Usuario")