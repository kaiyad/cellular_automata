import sys
import time

class Cell:
    def __init__(self, state: int = 1):
        self.state = state

    def apply_rule(self, count: int):
        old_state = self.state
        if count == 3 and self.state == 0:
            self.state = 1
        elif count in [2, 3] and self.state == 1:
            pass
        else:
            self.state = 0
        return self.state != old_state

class Grid:
    def __init__(self, grid_size: int = 20, grid: list[list[Cell]] = None):
        self.grid = grid if grid is not None else [[Cell() for _ in range(grid_size)] for _ in range(grid_size)]
        self.grid_size = grid_size if grid is None else len(self.grid)
        self.neighbours_count_grid = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]

    def update_neighbours_count_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                count = 0
                for x in range(max(0, i - 1), min(self.grid_size, i + 2)):
                    for y in range(max(0, j - 1), min(self.grid_size, j + 2)):
                        if (x, y) != (i, j):
                            count += self.grid[x][y].state
                self.neighbours_count_grid[i][j] = count

    def print_grid(self):
        sys.stdout.write("\033[H")
        for row in self.grid:
            for cell in row:
                sys.stdout.write(f"\033[1;37m{'*'}\033[0m " if cell.state == 1 else f"\033[1;30m{'.'}\033[0m ")
            sys.stdout.write("\n")
        sys.stdout.flush()
        time.sleep(0.5)

    def update_cell_states(self) -> bool:
        any_change = False
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.grid[i][j].apply_rule(self.neighbours_count_grid[i][j]):
                    any_change = True
        return any_change


if __name__ == "__main__":
    import random

    args = sys.argv[1:]
    grid_size = None
    if args:
        try:
            grid_size = int(args[0])
        except ValueError:
            print(f"Invalid grid size: {args[0]!r}", file=sys.stderr)
            sys.exit(1)
    if grid_size is None or grid_size < 1:
        grid_size = 20
    grid = Grid(grid_size=grid_size, grid=[[Cell(state=random.randint(0, 1)) for _ in range(grid_size)] for _ in range(grid_size)])
    grid.print_grid()

    while True:
        grid.update_neighbours_count_grid()
        if not grid.update_cell_states():
            break
        grid.print_grid()

    print("Reached equilibrium — grid is stable.")
