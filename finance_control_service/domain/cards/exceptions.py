class NameCardCannotBeEmpty(Exception):
    def __init__(self, message):
        self.message = message

class UserCardCannotBeEmpty(Exception):
    def __init__(self, message):
        self.message = message

class InvalidCardType(Exception):
    def __init__(self, message):
        self.message = message

class InvalidClosingDay(Exception):
    def __init__(self, message):
        self.message = message

class InvalidDueDay(Exception):
    def __init__(self, message):
        self.message = message

class CreditLimitCardMustBeGreaterThanZero(Exception):
    def __init__(self, message):
        self.message = message

class DescriptionCardCannotBeGreaterThan250Characters(Exception):
    def __init__(self, message):
        self.message = message

class CardUpdateRequiresExistingCardId(Exception):
    def __init__(self, message):
        self.message = message

class CardAlreadyExists(Exception):
    def __init__(self, message):
        self.message = message

class CardLastFourDigitsCannotBeEmpty(Exception):
    def __init__(self, message):
        self.message = message

class CardLastFourDigitsMustBeNumbers(Exception):
    def __init__(self, message):
        self.message = message
