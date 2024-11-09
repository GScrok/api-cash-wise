from django.db import models
from .base_model import BaseModel

class Card(BaseModel):
    CARD_TYPES = [
        ('credit', 'Cartão de Crédito'),
        ('debit', 'Cartão de Débito'),
    ]

    name = models.CharField(max_length=100)
    user = models.ForeignKey('finance_control.User', on_delete=models.CASCADE)
    card_last_four_digits = models.CharField(max_length=4)
    card_type = models.CharField(max_length=50, choices=CARD_TYPES)
    closing_day = models.IntegerField()
    due_day = models.IntegerField()
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    
    # campos de auditoria (opcional, mas recomendado)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} (*{self.card_last_four_digits})"

    class Meta:
        db_table = 'cards'
        app_label = 'finance_control'