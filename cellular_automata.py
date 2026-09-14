class Cell:
    def __init__(self, state: int = 1):
        self.state = state
        self.neighbours_count = 0

    def update_neighbours_count(self, new_count: int):
        self.neighbours_count = new_count
        if self.neighbours_count == 3 and self.state == 0:
            self.state = 1
            return
        elif self.neighbours_count in [2, 3] and self.state == 1:
            return
        self.state = 0

class Grid:
    def __init__(self, grid_size: int = 20, grid: list[list[Cell]] = None):
        self.grid_size = grid_size
        self.grid = grid if grid is not None else [[Cell() for _ in range(grid_size)] for _ in range(grid_size)]
        self.neighbours_count_grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

    def update_neighbours_count_grid(self):
        print("\nUpdating neighbours count grid...\n")
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                count = 0
                for x in range(max(0, i - 1), min(self.grid_size, i + 2)):
                    for y in range(max(0, j - 1), min(self.grid_size, j + 2)):
                        if (x, y) != (i, j):
                            count += self.grid[x][y].state
                self.neighbours_count_grid[i][j] = count

    def print_grid(self):
      for row in self.grid:
          print([cell.state for cell in row])

    def update_cell_states(self):
        print("\nUpdating cell states based on neighbours count...\n")
        for i in range(self.grid_size):
          for j in range(self.grid_size):
            self.grid[i][j].update_neighbours_count(self.neighbours_count_grid[i][j])





if __name__ == "__main__":
    import random
    grid = Grid(grid_size=20, grid=[[Cell(state=random.randint(0, 1)) for _ in range(20)] for _ in range(20)])
    grid.print_grid()

    for _ in range(3):
      print("\nUpdating neighbours count grid...\n")
      grid.update_neighbours_count_grid()
      for row in grid.neighbours_count_grid:
          print(row)
      grid.update_cell_states()
      grid.print_grid()









