class Transaction:
    def __init__(self, merchant, tag, description, amount, id=None):
        self.merchant = merchant
        self.tag = tag
        self.description = description
        self.amount = amount
        self.id = id