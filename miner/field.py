from miner.cell import Cell
# import miner.cell as script_name
import random

class Field:
    def __init__(self, size=20):
        self.data = [[Cell() for i in range(size)] for j in range(size)]
        self.size = 20

    def generate_field(self):
        # x = random.randint(0, self.size)
        # step 1
        mines_count = random.randint(self.size, self.size * 2)


        pairs = set()
        while len(pairs) < mines_count:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            pairs.add((x,y))

        # step 3
        for pair in pairs:
            x = pair[0]
            y = pair[1]
            self.data[x][y].mines_count = Cell.MINE

        for i in range(self.size):
            for j in range(self.size):
                self.calculate_mines_count(i,j)


    def calculate_mines_count(self, i, j):
        current_cell = self.data[i][j]
        count = 0
        if current_cell.mines_count != Cell.MINE:
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    x = i + dx
                    y = j + dy
                    if 0 <= x < self.size and 0 <= y < self.size and self.data[x][y].mines_count == Cell.MINE:
                        count += 1

            current_cell.mines_count = count

    def get_value(self, x, y):
        pass

    def open_cell(self, x, y):
        pass

field = Field()
field.generate_field()
