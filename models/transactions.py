class Transaction:
    def __init__(self, merchant, category, description, amount, id=None):
        self.merchant = merchant
        self.category = category
        self.description = description
        self.amount = amount
        self.id = id