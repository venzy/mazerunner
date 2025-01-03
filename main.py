from window import Window
from line import Line
from point import Point
from cell import Cell

def main():
    win: Window = Window(800, 600)

    x: int = 10
    y: int = 10

    all_walls = Cell(win, x, y, x + 20, y + 20)
    all_walls.draw()
    y += 30

    left_wall = Cell(win, x, y, x + 20, y + 20)
    left_wall.has_right_wall = False
    left_wall.has_top_wall = False
    left_wall.has_bottom_wall = False
    left_wall.draw()
    y += 30

    right_wall = Cell(win, x, y, x + 20, y + 20)
    right_wall.has_left_wall = False
    right_wall.has_top_wall = False
    right_wall.has_bottom_wall = False
    right_wall.draw()
    y += 30
    
    top_wall = Cell(win, x, y, x + 20, y + 20)
    top_wall.has_left_wall = False
    top_wall.has_right_wall = False
    top_wall.has_bottom_wall = False
    top_wall.draw()
    y += 30

    bottom_wall = Cell(win, x, y, x + 20, y + 20)
    bottom_wall.has_left_wall = False
    bottom_wall.has_right_wall = False
    bottom_wall.has_top_wall = False
    bottom_wall.draw()
    y += 30

    win.wait_for_close()

main()