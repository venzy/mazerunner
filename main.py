from window import Window
from line import Line
from point import Point

def main():
    win: Window = Window(800, 600)

    line_1: Line = Line(Point(10, 10), Point(40, 10))
    line_2: Line = Line(Point(20, 20), Point(400, 300))

    win.draw_line(line_1, "black")
    win.draw_line(line_2, "red")

    win.wait_for_close()

main()