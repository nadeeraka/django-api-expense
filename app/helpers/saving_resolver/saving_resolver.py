import functools
# from typing import List
# from app.models import Saving


class Saving:
    def __init__(self,rate,amount,time):
        self.rate = rate
        self.amount = amount
        self.time = time  # time in month


    def set_vars(self,r,a,t):
        self.rate = r
        self.amount = a
        self.time = t

    def calculate_savings(self):
        sum =  float(self.amount)/float(self.rate*self.time)
        return  sum/12

s = Saving(4,32000,1)
# s.set_vars(4,32000,1)
print(s.calculate_savings())




# def saving_resolver(savings: List[Saving]):
#     pass
#
# # for 0ne year
#
# def saving_reate(arg,t):
#     saving_list = list(arg)
#     if len(saving_list) == 0:
#         return  -1
#     sum_of_saving = functools.reduce(lambda a, b: a + b, saving_list)
#     if sum_of_saving < 50000:
#         return (sum_of_saving/100)*3
#     elif sum_of_saving < 499999.99:
#         return (sum_of_saving/100)*4
#     elif sum_of_saving > 500000:
#         return (sum_of_saving/100)*5