from django.db import models
from .base_model import BaseModel

class Subcategory(BaseModel):
    
    category = models.ForeignKey('finance_control.Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, null=True, blank=True)
    budget_limit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)