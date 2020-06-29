import functools
from typing import List
from app.models import Saving


def saving_resolver(savings: List[Saving]):
    pass

# for 0ne year

def saving_reate(arg,t):
    saving_list = list(arg)
    if len(saving_list) == 0:
        return  -1
    sum_of_saving = functools.reduce(lambda a, b: a + b, saving_list)
    if sum_of_saving < 50000:
        return (sum_of_saving/100)*3
    elif sum_of_saving < 499999.99:
        return (sum_of_saving/100)*4
    elif sum_of_saving > 500000:
        return (sum_of_saving/100)*5
