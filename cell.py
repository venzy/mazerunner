from window import Window
from line import Line
from point import Point

class Cell:
    def __init__(self, win: Window, x1: int, y1: int, x2: int, y2: int):
        self._win = win
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
    
    def draw(self, offset_x: int = 0, offset_y: int = 0):
        top_left = Point(self._x1 + offset_x, self._y1 + offset_y)
        top_right = Point(self._x2 + offset_x, self._y1 + offset_y)
        bottom_left = Point(self._x1 + offset_x, self._y2 + offset_y)
        bottom_right = Point(self._x2 + offset_x, self._y2 + offset_y)

        if self.has_left_wall:
            self._win.draw_line(Line(top_left, bottom_left), "black")
        if self.has_right_wall:
            self._win.draw_line(Line(top_right, bottom_right), "black")
        if self.has_top_wall:
            self._win.draw_line(Line(top_left, top_right), "black")
        if self.has_bottom_wall:
            self._win.draw_line(Line(bottom_left, bottom_right), "black")

    def draw_move(self, to_cell: "Cell", undo: bool = False, offset_x: int = 0, offset_y: int = 0):
        mid_from: Point = Point(
            self._x1 + ((self._x2 - self._x1) / 2) + offset_x,
            self._y1 + ((self._y2 - self._y1) / 2) + offset_y)
        mid_to: Point = Point(
            to_cell._x1 + ((to_cell._x2 - to_cell._x1) / 2) + offset_x,
            to_cell._y1 + ((to_cell._y2 - to_cell._y1) / 2) + offset_y)
        self._win.draw_line(Line(mid_from, mid_to), "grey" if undo else "red")
