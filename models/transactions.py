class Transaction:
    def __init__(self, merchant, category, description, amount, date, id=None):
        self.merchant = merchant
        self.category = category
        self.description = description
        self.amount = amount
        self.date = date
        self.id = id