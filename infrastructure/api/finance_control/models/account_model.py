from django.db import models
from .base_model import BaseModel

class Account(BaseModel):
    
    user = models.ForeignKey('finance_control.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    initial_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)