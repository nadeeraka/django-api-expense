import functools
from app.helpers.functions import select_min, select_mx


class Expenses:
    def __init__(self, expense=[]):
        self.expense = expense

    def set_expense(self, ex):
        self.expense = ex

    def calculate(self):
        return functools.reduce(lambda x, y: x + y, self.expense)

    def max_ex(self):
        return select_mx(self.expense)

    def min_ex(self):
        return select_min(self.expense)
