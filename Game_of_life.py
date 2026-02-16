import random
import time
import os

class GameOfLife:
    def __init__(self, rows, cols, wrap=True):
        self.rows = rows
        self.cols = cols
        self.wrap = wrap
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

    def randomize(self, density=0.3):
        for r in range(self.rows):
            for c in range(self.cols):
                self.grid[r][c] = 1 if random.random() < density else 0

    def count_neighbors(self, r, c):
        directions = [-1, 0, 1]
        count = 0

        for dr in directions:
            for dc in directions:
                if dr == 0 and dc == 0:
                    continue

                nr = r + dr
                nc = c + dc

                if self.wrap:
                    nr %= self.rows
                    nc %= self.cols
                else:
                    if not (0 <= nr < self.rows and 0 <= nc < self.cols):
                        continue

                count += self.grid[nr][nc]

        return count

    def next_generation(self):
        new_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        for r in range(self.rows):
            for c in range(self.cols):
                neighbors = self.count_neighbors(r, c)

                if self.grid[r][c] == 1:
                    if neighbors == 2 or neighbors == 3:
                        new_grid[r][c] = 1
                else:
                    if neighbors == 3:
                        new_grid[r][c] = 1

        self.grid = new_grid

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.grid:
            print(" ".join("⬛" if cell == 1 else "⬜" for cell in row))

    def run(self, generations=50, delay=0.3):
        for _ in range(generations):
            self.display()
            self.next_generation()
            time.sleep(delay)


# ====== MAIN PROGRAM ======

rows = 20
cols = 40

game = GameOfLife(rows, cols, wrap=True)
game.randomize(density=0.25)
game.run(generations=100, delay=0.2)
      
