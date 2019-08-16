from collections import Counter
from itertools import product


# generates data for the UI to plot.
class Plotter:

    roll_values = []
    roll_occurrences = []

    def __init__(self):
        pass

    def update_distribution_data(self, dice_list):
        self.roll_values.clear()
        self.roll_occurrences.clear()
        for item in self.generate_combos(dice_list):
            self.roll_values.append(item[0])
            self.roll_occurrences.append(item[1])

    # takes a list of ints and generates all possible outcomes of additive dice rolls and returns as a list.
    def generate_combos(self, dice_list):
        new_list = [n for n in dice_list if n != 0]
        possible = [[y for y in range(1, x + 1)] for x in new_list]
        result = [sum(x) for x in product(*possible)]

        count = Counter(result)
        return count.items()

    def get_roll_values(self):
        return self.roll_values

    def get_roll_occurrences(self):
        return self.roll_occurrences
