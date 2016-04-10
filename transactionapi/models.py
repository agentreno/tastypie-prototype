from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Transaction(models.Model):
    date = models.DateTimeField('date occurred')
    description = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    balance = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return str(self.date.date()) + ": " + str(self.amount) + " " + self.description
