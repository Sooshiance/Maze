from django.db import models


class Status:
    ToDo = 1
    Doing = 2
    Done = 3

    STATUS = (
        ('To Do', ToDo),
        ('Doing', Doing),
        ('Done', Done),
    )


class ToDo(models.Model):
    title   = models.CharField(max_length=50, unique=True)
    content = models.CharField(max_length=256)
    active  = models.BooleanField(default=True)
    status  = models.PositiveSmallIntegerField(default=1, choices=Status.STATUS)

    def __str__(self):
        return self.title
    
    class Meta:
        managed = True
        unique_together = ['title', 'content']
        verbose_name = 'To Do'
        verbose_name_plural = 'To Dos'
