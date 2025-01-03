from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze

def main():
    win: Window = Window(800, 600)

    maze: Maze = Maze(10, 10, 8, 5, 20, 20, win)

    win.wait_for_close()

main()