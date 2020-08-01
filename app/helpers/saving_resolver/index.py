import functools
# from typing import List
# from app.models import Saving
from app.helpers.util import calculate


def cal_rate(amount, rate):
    return (amount * rate) / 100


def calculate_saving_algo(amount):
    if amount < 50000:
        return cal_rate(amount, 3)
    if 50000 < amount < 500000:
        return cal_rate(amount, 4)
    if amount > 500000:
        return cal_rate(amount, 5)
    return 0


def calculate_savings(amount_array, months):
    amount = calculate(amount_array)
    print('amount', amount)
    val = calculate_saving_algo(amount) / months
    print('with rate', val)
    full_amount = val + amount
    print('full amount', full_amount)
    return round(full_amount, 2)


def get_only_rate(amount_array, months):
    amount = calculate(amount_array)
    print('amount', amount)
    return calculate_saving_algo(amount) / months
