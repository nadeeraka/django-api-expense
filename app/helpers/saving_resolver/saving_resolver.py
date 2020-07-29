import functools
# from typing import List
# from app.models import Saving
from app.helpers.util import calculate


class Saving:

    def calculate_saving_algo(self, amount):
        rate = 0
        if amount < 50000:
            rate = 3
        elif 499999.99 < amount > 50000:
            rate = 4

        elif amount > 499999.99:
            rate = 5
        return rate * amount

    def calculate_savings(self, amount_array, months):
        amount = calculate(amount_array)
        return self.calculate_saving_algo(amount) / months
