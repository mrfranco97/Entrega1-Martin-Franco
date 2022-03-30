from django.db import models
from django.forms import PasswordInput

# Create your models here.

#Cada Post tiene un Autor
class Post(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=120)
    categorie = models.CharField(max_length=15)

#Author hereda de user
#Y tiene un listado de Post
class Author(models.Model):
    fullname = models.CharField(max_length=30)


class User(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(PasswordInput,max_length=20)
