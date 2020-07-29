
from app.helpers.saving_resolver.index import calculate_savings, calculate_saving_algo


class Saving:

    def get_normal_savings(self, amount_array, months):
        return calculate_savings(self, amount_array, months)
