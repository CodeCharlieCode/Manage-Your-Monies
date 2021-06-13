class User:
    def __init__(self, name, balance, total_budget, category_budget, id=None):
        self.name = name
        self.balance = balance
        self.total_budget = total_budget
        self.category_budget = category_budget
        self.id = id

    #Think about using joining tables to link a category budget cateogries and users