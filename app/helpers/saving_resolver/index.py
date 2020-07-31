import functools
# from typing import List
# from app.models import Saving
from app.helpers.util import calculate


def calculate_saving_algo(amount):
    if amount < 50000:
        return 3 * amount
    elif 499999.99 < amount > 50000:
        return 4 * amount
    elif amount > 499999.99:
        return 5 * amount


def calculate_savings(amount_array, months):
    amount = calculate(amount_array)
    print('amount', amount)
    val = calculate_saving_algo(amount) / months
    print('with rate', val)
    full_amount = val + amount
    print('full amount', full_amount)
    return full_amount
