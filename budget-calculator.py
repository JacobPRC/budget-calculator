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

# calculate expenses vs savings compares to ratio and give recommendation if they should save more or are good
# visually show this to user in a pie chart
# error handle


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
            print("Program has been stopped due to invalid response. Please run again")
            return


def budget_calculator():
    print("Welcome to the budget calculator! We're going to ask you questions about your monthly spending and tell you how much you'll have left to save.")
    print("How much do you earn a month?")
    paycheck = idiot_proof(input())
    if(paycheck == None):
        return
    print("How much do you spend on groceries a month?")
    groceries = idiot_proof(input())
    if(groceries == None):
        return
    print("How much do you spend on reoccuring bills?")
    bills = idiot_proof(input())
    if(bills == None):
        return
    print("How much do you spend on yourself?")
    personal = idiot_proof(input())
    if(personal == None):
        return
    print("Anything else you spend per month? If yes, enter the amount, if no enter 0")
    extra = idiot_proof(input())
    if(extra == None):
        return
    user_budget = Budget(paycheck, groceries, bills, personal, extra)
    amt_left = str(user_budget.how_much_left())
    print("You will have $" + amt_left + " after all of your expenses")


budget_calculator()
