from app.helpers import util


class Expenses:
    def __init__(self, expense=[]):
        self.expense = expense

    def set_expense(self, ex):
        self.expense = ex

    def calculate(self):
        return util.cal(self.expense)

    def max_ex(self):
        return util.select_mx(self.expense)

    def min_ex(self):
        return util.select_min(self.expense)

x =[1220,300,5678,378]
ex = Expenses()
ex.set_expense(x)
print(ex.calculate())