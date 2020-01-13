from miner.cell import Cell
# import miner.cell as script_name
import random

class Field:
    def __init__(self, size=7):
        self.data = [[Cell() for i in range(size)] for j in range(size)]
        self.size = 7
    def generate_field(self):
        x = random.randint(0, self.size)


    def get_value(self, x, y):
        pass

    def open_cell(self, x, y):
        pass

