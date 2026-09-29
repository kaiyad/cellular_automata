class Grid:
    def __init__(self, grid_size: int = 20, grid: list[list[Cell]] = None):
        self.grid = grid if grid is not None else [[Cell() for _ in range(grid_size)] for _ in range(grid_size)]
        self.grid_size = grid_size if grid is None else len(self.grid)
        self.neighbours_count_grid = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]

    def apply_rule_30(self):
        new_grid = [[Cell() for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                left = self.grid[i][j - 1].state if j > 0 else 0
                center = self.grid[i][j].state
                right = self.grid[i][j + 1].state if j < self.grid_size - 1 else 0
                new_grid[i][j].state = self.rule_30(left, center, right)
        self.grid = new_grid

    @staticmethod
    def rule_30(left: int, center: int, right: int) -> int:
        return left ^ (center or right)

    def print_grid(self):
        for row in self.grid:
            for cell in row:
                sys.stdout.write(f"\033[1;37m{'*'}\033[0m " if cell.state == 1 else f"\033[1;30m{'.'}\033[0m ")
            sys.stdout.write("\n")
        time.sleep(0.5)

    def convert_to_decimal(self) -> int:
        decimal_value = 0
        j = self.grid_size // 2  # Middle column
        for i in range(self.grid_size):
            decimal_value += self.grid[i][j].state * (2 ** (self.grid_size - 1 - i))
        return decimal_value


class Cell:
    def __init__(self, state: int = 0):
        self.state = state


if __name__ == "__main__":
    import random
    import sys
    import time

    args = sys.argv[1:]
    grid_size = None
    if args:
        try:
            grid_size = int(args[0])
        except ValueError:
            print("Invalid grid size. Using default size of 20.")
            grid_size = 20
    else:
        grid_size = 20

    # Initialize the grid with random states
    initial_grid = [[Cell(random.randint(0, 1)) for _ in range(grid_size)] for _ in range(grid_size)]
    grid = Grid(grid_size=grid_size, grid=initial_grid)

    print(grid.convert_to_decimal())
    grid.apply_rule_30()
    print(grid.convert_to_decimal())
