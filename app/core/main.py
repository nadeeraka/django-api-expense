from app.helpers.util import select_min, select_mx, calculate, average


class Generics:
    def __init__(self, expense=[]):
        self.expense = expense

    def set_expense(self, ex):
        self.expense = ex

    def calculate(arg):
        return calculate(arg)

    def max_ex(arg):
        return select_mx(arg)

    def min_ex(arg):
        return select_min(arg)

    def average_ex(arg):
        return average(arg)
