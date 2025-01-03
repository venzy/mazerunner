from window import Window
from cell import Cell
import time
from typing import Optional

class Maze:
    def __init__(self, x1: int, y1: int, num_rows: int, num_cols: int, cell_size_x: int, cell_size_y: int, win: Optional[Window] = None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        self._cells: list[list[Cell]] = []
        # Each top-level list is a column of Cell objects.
        # Cell coordinates are relative to the maze.
        # TODO change the walls of each cell?
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
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        entrance: Cell = self._cells[0][0]
        exit: Cell = self._cells[-1][-1]

        entrance.has_top_wall = False
        exit.has_bottom_wall = False

        if self._win:
            self._draw_cell(0, 0)
            self._draw_cell(self._num_rows - 1, self._num_cols - 1)