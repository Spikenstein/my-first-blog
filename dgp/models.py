from django.db import models
from django.utils import timezone

from .choices import *

class Run(models.Model):
    user = models.ForeignKey('auth.User')
    date = models.DateTimeField(default=timezone.now)

    typeCol = models.TextField()
    target  = models.TextField()

    log = models.TextField()

    def __str__(self):
        return self.typeCol+" "+self.target
