import functools
# from typing import List
# from app.models import Saving
from app.helpers.util import calculate


def calculate_saving_algo(amount):

    amount_in_int = int(amount)
    if amount_in_int < 50000:
        return 3 * amount_in_int
    elif 500000 < amount_in_int > 50000:
        print('called')
        return 4 * amount_in_int
    elif amount_in_int > 500000:
        return 5 * amount_in_int
    return amount_in_int


def calculate_savings(amount_array, months):
    amount = calculate(amount_array)
    print('amount', amount)
    val = calculate_saving_algo(amount)
    print('with rate', val)
    full_amount = val + amount
    print('full amount', full_amount)
    return full_amount
