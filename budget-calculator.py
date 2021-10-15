import matplotlib.pyplot as plt
import numpy as np


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

    def percentage(self, category):
        return 100 * float(category)/float(self.paycheck)

    def show_spending(self, amt_left):
        # Can I DRY this out with a loop?

        grocery_percentage = self.percentage(self.groceries)
        bills_percentage = self.percentage(self.bills)
        personal_percentage = self.percentage(self.personal)
        extra_percentage = self.percentage(self.extra)
        left_over_percentage = self.percentage(amt_left)

        labels = 'Groceries', 'Bills', 'Personal', 'Extra', 'Amount left for savings'
        sizes = [grocery_percentage, bills_percentage,
                 personal_percentage, extra_percentage, left_over_percentage]
        explode = (0, 0, 0, 0, 0.1)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels,
                autopct='%1.1f%%', shadow=True, startangle=90)
        ax1.axis('equal')

        plt.show()


def idiot_proof(num):
    try:
        correct_num = float(num)
        return correct_num
    except ValueError:
        print("Please enter a number")
        try:
            num = float(input())
            return num
        except:
            raise Exception(
                "Program has been stopped due to invalid response. Please run again")


def budget_calculator():
    print("Welcome to the budget calculator! We're going to ask you questions about your monthly spending and tell you how much you'll have left to save.")

    print("How much do you earn a month?")
    paycheck = idiot_proof(input())

    print("How much do you spend on groceries a month?")
    groceries = idiot_proof(input())

    print("How much do you spend on reoccuring bills?")
    bills = idiot_proof(input())

    print("How much do you spend on yourself?")
    personal = idiot_proof(input())

    print("Anything else you spend per month? If yes, enter the amount, if no enter 0")
    extra = idiot_proof(input())

    user_budget = Budget(paycheck, groceries, bills, personal, extra)
    amt_left = user_budget.how_much_left()
    print(f"You will have ${amt_left} after all of your expenses")

    if amt_left > 0:
        percent_saved = float(
            np.round(user_budget.percentage(amt_left), 1))
        if percent_saved < 20.0:
            print(
                f"It looks like you aren't saving a whole lot. We recommend saving 20% of your paycheck, but you are only saving {percent_saved}%")
        else:
            print(
                f"Good job budgeting! You are saving {percent_saved}% of your paycheck")

        print("Would you like to see your spending visually represented? y/n")
        if str(input()).lower() == "y":
            user_budget.show_spending(amt_left)
        else:
            print("Thanks for budgeting with us!")
    else:
        print("It seems like you're spending more than you make! Time to think about adjusting your spending")


budget_calculator()
