import functools

import django


def valdate(x):
    if x is not None:
        print(type(x))
        if type(x) == int:
            if x > 0:
                return True
            else:
                return 0
        elif type(x) == list:
            if len(x) > 0:
                return True
            else:
                return []
        if type(x) == django.db.models.query.QuerySet:
            return True

    return False


def calculate(arr):
    if not valdate(arr):
        return False
    return functools.reduce(lambda x, y: x + y, arr)


def select_mx(arr):
    x = 0
    for e in arr:
        if e > x:
            x = e
    return x


def select_min(arr):
    if not valdate(arr):
        return False
    x = arr[0]
    for e in arr:
        if x > e:
            x = e
    return x


def average(arr):
    if not valdate(arr):
        return False
    return calculate(arr) / len(arr)