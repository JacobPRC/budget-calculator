class Budget:

    def __init__(self, paycheck, groceries, bills, personal, extra):
        self.paycheck = paycheck
        self.groceries = groceries
        self.bills = bills
        self.personal = personal
        self.extra = extra

    def how_much_left(self):
        expenses = self.groceries + self.bills + self.personal + self.extra
        left_over = self.paycheck - expenses
        return left_over
