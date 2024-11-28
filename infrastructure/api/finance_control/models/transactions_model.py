from django.db import models
from .base_model import BaseModel

class Transaction(BaseModel):
    TRANSACTION_TYPES = [
            ('incoming', 'Incoming'),
            ('expense', 'Expense')
        ]

    user = models.ForeignKey('finance_control.User', on_delete=models.CASCADE)
    category = models.ForeignKey('finance_control.Category', on_delete=models.CASCADE)
    subcategory = models.ForeignKey('finance_control.Subcategory', on_delete=models.CASCADE, null=True, blank=True)
    card = models.ForeignKey('finance_control.Card', on_delete=models.CASCADE, null=True, blank=True)
    account = models.ForeignKey('finance_control.Account', on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    transaction_date = models.DateField()
    