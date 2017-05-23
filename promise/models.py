# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class PromiseModel(models.Model):
    createdDate = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    promise = models.CharField(max_length=100)

    class Meta:
        ordering = ('createdDate',)
