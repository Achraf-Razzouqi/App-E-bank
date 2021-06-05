from django.db import models
from account.models import Use
# Create your models here.

class Operation(models.Model):
    TYPE = (
        ('Credit', 'Credit'),
        ('Debit', 'Debit')
    )
    idR = models.ForeignKey(Use, on_delete=models.CASCADE, related_name= 'idR',default= None)
    idD = models.ForeignKey(Use, on_delete=models.CASCADE, related_name='idD', default=None)
    solde = models.FloatField(null=True)
    type = models.CharField(max_length=50, null=True, choices=TYPE)
    operation= models.CharField(max_length=30, null= True)
    telephobe=models.CharField(max_length=30, null= True)
    Adate=models.CharField(max_length=30, null= True)