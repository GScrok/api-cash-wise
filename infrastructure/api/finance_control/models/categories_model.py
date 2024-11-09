from django.db import models
from .base_model import BaseModel

class Category(BaseModel):
    name = models.CharField(max_length=100)
    user = models.ForeignKey('finance_control.User', on_delete=models.CASCADE)
    description = models.CharField(max_length=250, null=True, blank=True)
    budget_limit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'categories'
        app_label = 'finance_control'