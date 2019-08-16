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
        new_list = self.clear_empty_dice(dice_list)
        i = self.get_iterations(new_list)
        for item in self.generate_combos(new_list):
            self.roll_values.append(item[0])
            self.roll_occurrences.append(self.get_probability(item[1], i))


    # takes a list of ints and generates all possible outcomes of additive dice rolls and returns as a list.
    def generate_combos(self, dice_list):
        possible = [[y for y in range(1, x + 1)] for x in dice_list]
        result = [sum(x) for x in product(*possible)]

        count = Counter(result)
        return count.items()

    def clear_empty_dice(self, dice_list):
        result = [n for n in dice_list if n != 0]  # take out empty dice slots
        return result

    def get_roll_values(self):
        return self.roll_values

    def get_roll_occurrences(self):
        return self.roll_occurrences

    def get_probability(self, value, iterations):
        i = value/iterations*100
        i = round(i, 4)
        return str(i)+'%'

    def get_iterations(self, dice_list):
        new_list = self.clear_empty_dice(dice_list)
        result = 1
        for die in new_list:
            result *= die
        return result
