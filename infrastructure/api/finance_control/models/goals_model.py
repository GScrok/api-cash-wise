from django.db import models
from .base_model import BaseModel

class Goal(BaseModel):

    name        = models.CharField(max_length=100)
    user        = models.ForeignKey('finance_control.User', on_delete=models.CASCADE)
    category    = models.ForeignKey('finance_control.Category', on_delete=models.CASCADE, null=True, blank=True)
    value       = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)
    start_at    = models.DateTimeField()
    end_at      = models.DateTimeField()