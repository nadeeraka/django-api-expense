
from app.helpers.saving_resolver.index import calculate_savings, calculate_saving_algo


class Saving_resolver:
    def __init__(self, savings=[]):
        self.savings = savings

    def get_normal_savings( amount_array, months):
        return calculate_savings( amount_array, months)
