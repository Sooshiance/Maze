from django.db import models
from enum import Enum


class Status(Enum):
    ToDo = 1
    Doing = 2
    Done = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name.replace('_', ' ')) for key in cls]


class ToDo(models.Model):
    title   = models.CharField(max_length=50, unique=True)
    content = models.CharField(max_length=256)
    active  = models.BooleanField(default=True)
    status  = models.PositiveSmallIntegerField(default=1, choices=Status.choices())

    def __str__(self):
        return self.title
    
    class Meta:
        managed = True
        unique_together = ['title', 'content']
        verbose_name = 'To Do'
        verbose_name_plural = 'To Dos'
