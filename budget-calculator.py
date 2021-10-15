import matplotlib.pyplot as plt


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

    # In this code we need to reference left over amt in above function. Instead of calling this function twice, I will use the
    # amt_left variable calculated in budget_calculator function.

    def show_spending(self, amt_left):
        # Can I DRY this out with a loop?

        grocery_percentage = percentage(self.groceries, self.paycheck)
        bills_percentage = percentage(self.bills, self.paycheck)
        personal_percentage = percentage(self.personal, self.paycheck)
        extra_percentage = percentage(self.extra, self.paycheck)
        left_over_percentage = percentage(amt_left, self.paycheck)

        labels = 'Groceries', 'Bills', 'Personal', 'Extra', 'Amount left for savings'
        sizes = [grocery_percentage, bills_percentage,
                 personal_percentage, extra_percentage, left_over_percentage]
        explode = (0, 0, 0, 0, 0.1)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels,
                autopct='%1.1f%%', shadow=True, startangle=90)
        ax1.axis('equal')

        plt.show()

        # calculate expenses vs savings compares to ratio and give recommendation if they should save more or are good
        # visually show this to user in a pie chart
        # only show pie if positive number
        # change input if positive or negative


def percentage(part, whole):
    return 100 * float(part)/float(whole)


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
        print("Would you like to see this visually represented? y/n")
        if str(input()).lower() == "y":
            user_budget.show_spending(amt_left)
        else:
            print("Thanks for budgeting with us!")
    else:
        print("It seems like you're spending more than you make! Time to think about adjusting your spending")


budget_calculator()
