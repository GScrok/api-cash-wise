class TransactionException(Exception):
    def __init__(self, message):
        self.message = message

class UserTransactionCannotBeEmpty(Exception):
    def __init__(self, message):
        self.message = message

class AccountTransactionCannotBeEmpty(Exception):
    def __init__(self, message):
        self.message = message

class CategoryTransactionCannotBeEmpty(Exception):
    def __init__(self, message):
        self.message = message

class TypeTransactionCannotBeEmpty(Exception):
    def __init__(self, message):
        self.message = message

class AmountTransactionCannotBeEmpty(Exception):
    def __init__(self, message):
        self.message = message

class DescriptionTransactionCannotBeEmpty(Exception):
    def __init__(self, message):
        self.message = message

class TransactionDateCannotBeEmpty(Exception):
    def __init__(self, message):
        self.message = message

class TransactionDateMustBeValid(Exception):
    def __init__(self, message):
        self.message = message

class DescriptionTransactionCannotBeGreaterThan250Characters(Exception):
    def __init__(self, message):
        self.message = message

class TransactionAmountMustBeGreaterThanZero(Exception):
    def __init__(self, message):
        self.message = message

class InvalidTransactionType(Exception):
    def __init__(self, message):
        self.message = message

        