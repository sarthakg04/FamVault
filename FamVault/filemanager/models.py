# models.py
from django.db import models

class Folder(models.Model):
    name = models.CharField(max_length=100)

class File(models.Model):
    name = models.CharField(max_length=100)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
