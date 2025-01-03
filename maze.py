from window import Window
from cell import Cell
from line import Line
from point import Point
import time, random
from typing import Optional

class Maze:
    def __init__(
            self,
            x1: int,
            y1: int,
            num_rows: int,
            num_cols: int,
            cell_size_x: int,
            cell_size_y: int,
            win: Optional[Window] = None,
            seed: Optional[int] = None
            ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            random.seed(seed)

        self._animate_step = 0.001

        self._create_cells()

    def _create_cells(self):
        self._cells: list[list[Cell]] = []
        # Each top-level list is a column of Cell objects.
        # Cell coordinates are relative to the maze.
        for col in range(self._num_cols):
            self._cells.append([])
            cell_left = col * self._cell_size_x
            cell_right = cell_left + self._cell_size_x
            for row in range(self._num_rows):
                cell_top = row * self._cell_size_y
                cell_bottom = cell_top + self._cell_size_y
                col_list: list[Cell] = self._cells[col]
                col_list.append(Cell(cell_left, cell_top, cell_right, cell_bottom, self._win))

        if self._win:
            for col in range(self._num_cols):
                for row in range(self._num_rows):
                    self._draw_cell(row, col)
    
    def _draw_cell(self, row, col):
        cell: Cell = self._cells[col][row]
        cell.draw(self._x1, self._y1)
        self._animate()
    
    def _animate(self):
        if not self._win:
            raise Exception("_animate() called without window")
        self._win.redraw()
        time.sleep(self._animate_step)
    
    def _break_entrance_and_exit(self):
        entrance: Cell = self._cells[0][0]
        exit: Cell = self._cells[-1][-1]

        entrance.has_top_wall = False
        exit.has_bottom_wall = False

        if self._win:
            self._draw_cell(0, 0)
            self._draw_cell(self._num_rows - 1, self._num_cols - 1)
    
    def _break_walls_r(self, row, col):
        cell: Cell = self._cells[col][row]
        cell.visited = True
        while True:
            to_visit: list[tuple[int, int]] = []
            # Left
            if col > 0 and not self._cells[col - 1][row].visited:
                to_visit.append((row, col - 1))
            # Right
            if col < (self._num_cols - 1) and not self._cells[col + 1][row].visited:
                to_visit.append((row, col + 1))
            # Up
            if row > 0 and not self._cells[col][row - 1].visited:
                to_visit.append((row - 1, col))
            # Down
            if row < (self._num_rows - 1) and not self._cells[col][row + 1].visited:
                to_visit.append((row + 1, col))
            
            if not len(to_visit):
                if self._win:
                    self._draw_cell(row, col)
                return
            
            selected_visit = random.randrange(len(to_visit))
            (visit_row, visit_col) = to_visit[selected_visit]
            visit_cell: Cell = self._cells[visit_col][visit_row]
            if visit_cell._x1 < cell._x1:
                # Left of current
                cell.has_left_wall = False
                visit_cell.has_right_wall = False
            elif visit_cell._x1 > cell._x1:
                # Right of current
                cell.has_right_wall = False
                visit_cell.has_left_wall = False
            elif visit_cell._y1 < cell._y1:
                # Above current
                cell.has_top_wall = False
                visit_cell.has_bottom_wall = False
            elif visit_cell._y1 > cell._y1:
                # Below current
                cell.has_bottom_wall = False
                visit_cell.has_top_wall = False
            else:
                raise Exception("Trying to break down walls but got the logic wrong")

            self._break_walls_r(visit_row, visit_col)

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
    
    def solve(self) -> bool:
        if self._win:
            # Draw line from outer edge to middle of entrance cell
            self._win.draw_line(
                Line(
                    Point(
                        self._x1 + (self._cell_size_x / 2),
                        self._y1
                        ),
                    Point(
                        self._x1 + (self._cell_size_x / 2),
                        self._y1 + (self._cell_size_y / 2)
                        ),
                    ),
                "red"
                )
        if self._solve_r(0, 0):
            if self._win:
                # Draw line from middle of exit cell to outer edge
                self._win.draw_line(
                    Line(
                        Point(
                            self._x1 + (self._cell_size_x * (self._num_cols - 0.5)),
                            self._y1 + (self._cell_size_y * (self._num_rows - 0.5))
                            ),
                        Point(
                            self._x1 + (self._cell_size_x * (self._num_cols - 0.5)),
                            self._y1 + (self._cell_size_y * self._num_rows)
                            ),
                        ),
                    "red"
                    )

            return True

        return False
    
    def _solve_r(self, row, col) -> bool:
        self._animate()
        cell: Cell = self._cells[col][row]
        cell.visited = True

        # Check if we're at the exit
        if (row, col) == (self._num_rows - 1, self._num_cols - 1):
            return True

        # Check left
        if col > 0 and not cell.has_left_wall:
            left_cell: Cell = self._cells[col - 1][row]
            if not left_cell.visited and not left_cell.has_right_wall:
                cell.draw_move(left_cell, False, self._x1, self._y1)
                if self._solve_r(row, col - 1):
                    return True
                cell.draw_move(left_cell, True, self._x1, self._y1)

        # Check right
        if col < self._num_cols - 1 and not cell.has_right_wall:
            right_cell: Cell = self._cells[col + 1][row]
            if not right_cell.visited and not right_cell.has_left_wall:
                cell.draw_move(right_cell, False, self._x1, self._y1)
                if self._solve_r(row, col + 1):
                    return True
                cell.draw_move(right_cell, True, self._x1, self._y1)

        # Check up
        if row > 0 and not cell.has_top_wall:
            above_cell: Cell = self._cells[col][row - 1]
            if not above_cell.visited and not above_cell.has_bottom_wall:
                cell.draw_move(above_cell, False, self._x1, self._y1)
                if self._solve_r(row - 1, col):
                    return True
                cell.draw_move(above_cell, True, self._x1, self._y1)

        # Check down
        if row < self._num_rows - 1 and not cell.has_bottom_wall:
            below_cell: Cell = self._cells[col][row + 1]
            if not below_cell.visited and not below_cell.has_top_wall:
                cell.draw_move(below_cell, False, self._x1, self._y1)
                if self._solve_r(row + 1, col):
                    return True
                cell.draw_move(below_cell, True, self._x1, self._y1)

        # No solution from this cell
        return False