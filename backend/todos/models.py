from __future__ import annotations
from django.db import models



class Todo(models.Model):
    title: models.CharField[str, str] = models.CharField(max_length=200) 
    body: models.TextField[str, str] = models.TextField() 

    def __str__(self) -> str:
        return self.title