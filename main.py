from window import Window
from maze import Maze

def main():
    win: Window = Window(800, 600)

    maze: Maze = Maze(10, 10, 29, 39, 20, 20, win)
    maze._break_entrance_and_exit()
    maze._animate_step = 0.005
    maze._break_walls_r(0, 0)
    maze._reset_cells_visited()
    maze._animate_step = 0.01
    maze.solve()

    win.wait_for_close()

main()