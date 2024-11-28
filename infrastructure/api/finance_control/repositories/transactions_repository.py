from finance_control_service.application.user.user_dto import UserDTO
from finance_control_service.application.transactions.transactions_storage import TransactionStorage
from finance_control_service.application.transactions.transactions_dto import TransactionDTO
from finance_control.models import Account, Card, Category, Subcategory, Transaction, User

from uuid import UUID

class TransactionRepository(TransactionStorage):
    
    def _dto_to_model(self, transaction_dto: TransactionDTO) -> Transaction:
        account = Account.objects.get(pk=transaction_dto.account_id)
        category = Category.objects.get(pk=transaction_dto.category_id)
        subcategory = Subcategory.objects.filter(pk=transaction_dto.subcategory_id).first()
        card = Card.objects.filter(pk=transaction_dto.card_id).first()

        user = User.objects.get(pk=transaction_dto.user.id)

        transaction                  = Transaction()
        transaction.id               = transaction_dto.id
        transaction.user             = user
        transaction.category         = category
        transaction.subcategory      = subcategory
        transaction.card             = card
        transaction.account          = account
        transaction.amount           = transaction_dto.amount
        transaction.type             = transaction_dto.type
        transaction.description      = transaction_dto.description
        transaction.transaction_date = transaction_dto.transaction_date

        return transaction
    
    def _model_to_dto(self, transaction: Transaction) -> TransactionDTO:        
        return TransactionDTO({
            'id'              : transaction.id,
            'account_id'      : transaction.account.id,
            'category_id'     : transaction.category.id,
            'subcategory_id'  : transaction.subcategory.id if transaction.subcategory else None,
            'card_id'         : transaction.card.id if transaction.card else None,
            'amount'          : transaction.amount,
            'type'            : transaction.type,
            'description'     : transaction.description,
            'transaction_date': transaction.transaction_date,
        })
    
    def get_by_id(self, id: UUID) -> TransactionDTO:
        return self._model_to_dto(Transaction.objects.get(pk=id))
    
    def get_all(self) -> list[TransactionDTO]:
        transactions = Transaction.objects.all()
        return [self._model_to_dto(transaction) for transaction in transactions]

    def get_all_by_category(self, category_id: UUID) -> list[TransactionDTO]:
        transactions = Transaction.objects.filter(category=category_id)
        return [self._model_to_dto(transaction) for transaction in transactions]

    def get_all_by_subcategory(self, subcategory_id: UUID) -> list[TransactionDTO]:
        transactions = Transaction.objects.filter(subcategory=subcategory_id)
        return [self._model_to_dto(transaction) for transaction in transactions]
    
    def validate_funds_for_transaction(self, transaction_dto: TransactionDTO, user_id: UUID):
        amount = Account.objects.get(pk=transaction_dto.account_id).initial_balance
        list_transaction = Transaction.objects.filter(user=user_id)
        for transaction in list_transaction:
            if transaction.type == 'Incoming':
                amount += transaction.amount
            elif transaction.type == 'Expense':
                amount -= transaction.amount

        return amount >= transaction_dto.amount

    def save(self, transaction_dto) -> TransactionDTO:
        transaction = self._dto_to_model(transaction_dto)
        transaction.save()
        return self._model_to_dto(transaction)
    
    def update(self, transaction_dto: TransactionDTO) -> TransactionDTO:
        transaction = Transaction.objects.get(pk=transaction_dto.id)

        account = Account.objects.get(pk=transaction_dto.account_id)
        category = Category.objects.get(pk=transaction_dto.category_id)
        subcategory = Subcategory.objects.filter(pk=transaction_dto.subcategory_id).first()
        card = Card.objects.filter(pk=transaction_dto.card_id).first()
        
        transaction.card = card
        transaction.account = account
        transaction.category = category
        transaction.subcategory = subcategory
        transaction.type = transaction_dto.type
        transaction.amount = transaction_dto.amount
        transaction.description = transaction_dto.description
        transaction.transaction_date = transaction_dto.transaction_date
        transaction.save()
        
        return self._model_to_dto(transaction)
    
    def delete(self, id: UUID) -> bool:
        transaction = Transaction.objects.get(pk=id)
        transaction.delete()
        return True