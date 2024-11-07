from datetime import datetime
from typing import Optional
from finance_control_service.application.transactions.transaction_store_dto import TransactionDto

class Transaction(object):
    
    id: int
    user_id: int
    account_id: int
    category_id: int
    type: str
    amount: float
    currency: str
    transaction_date: datetime
    description: Optional[str] 
    status: bool
    
    def __init__(self, transactionDto: TransactionDto) -> None:
        self.id               = transactionDto.id
        self.user_id          = transactionDto.user_id
        self.account_id       = transactionDto.account_id
        self.category_id      = transactionDto.category_id
        self.type             = transactionDto.type
        self.amount           = transactionDto.amount
        self.currency         = transactionDto.currency
        self.transaction_date = transactionDto.transaction_date
        self.description      = transactionDto.description
        self.status           = transactionDto.status