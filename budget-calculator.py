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


def budget_calculator():
    print("Welcome to the budget calculator! We're going to ask you questions about your monthly spending and tell you how much you'll have left to save.")
    print("How much do you earn a month?")
    paycheck = int(input())
    print("How much do you spend on groceries a month?")
    groceries = int(input())
    print("How much do you spend on reoccuring bills?")
    bills = int(input())
    print("How much do you spend on yourself?")
    personal = int(input())
    print("Anything else you spend per month? If yes, enter the amount, if no enter 0")
    extra = int(input())
    user_budget = Budget(paycheck, groceries, bills, personal, extra)
    amt_left = str(user_budget.how_much_left())
    print("You will have $" + amt_left + " after all of your expenses")


budget_calculator()
