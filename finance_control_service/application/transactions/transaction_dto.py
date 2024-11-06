from typing import Optional
from datetime import datetime
from finance_control_service.domain.transaction.entities import Transaction

class TransactionDto(object):

    id: Optional[int]
    user_id: int
    account_id: int
    category_id: int
    type: str
    amount: float
    currency: str
    transaction_date: datetime
    description: Optional[str] 
    status: bool

    def __init__(self, data: dict) -> None:
        self.id               = data.get('id', None)
        self.user_id          = data.get('user_id')
        self.account_id       = data.get('account_id')
        self.category_id      = data.get('category_id')
        self.type             = data.get('type')
        self.amount           = data.get('amount')
        self.currency         = data.get('currency')
        self.transaction_date = data.get('transaction_date')
        self.description      = data.get('description')
        self.status           = data.get('status')
