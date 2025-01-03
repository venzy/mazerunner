import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        row_col_combos = [
            (10, 12),
            (29, 39),
            (40, 30)
        ]
        for (num_rows, num_cols) in row_col_combos:
            m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
            self.assertEqual(
                len(m1._cells),
                num_cols,
            )
            self.assertEqual(
                len(m1._cells[0]),
                num_rows,
            )
        
        # We don't currently test that the Maze creation rejects parameters that
        # would exceed the bounds of the canvas.

    def test_maze_entrance_exit(self):
        row_col_combos = [
            (10, 12),
            (29, 39),
            (40, 30)
        ]
        for (num_rows, num_cols) in row_col_combos:
            m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
            m1._break_entrance_and_exit()

            entrance = m1._cells[0][0]
            self.assertFalse(entrance.has_top_wall)
            self.assertTrue(entrance.has_left_wall)
            self.assertTrue(entrance.has_right_wall)
            self.assertTrue(entrance.has_bottom_wall)

            exit = m1._cells[-1][-1]
            self.assertFalse(exit.has_bottom_wall)
            self.assertTrue(exit.has_top_wall)
            self.assertTrue(exit.has_left_wall)
            self.assertTrue(exit.has_right_wall)
        
        # We don't currently test that the Maze creation rejects parameters that
        # would exceed the bounds of the canvas.

    def test_maze_break_walls(self):
        row_col_combos = [
            (10, 12),
            (29, 39),
            (40, 30)
        ]
        for (num_rows, num_cols) in row_col_combos:
            m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None, 0)
            m1._break_entrance_and_exit()
            m1._break_walls_r(0, 0)
            # We don't actually check values, just that it completes.
            for col in m1._cells:
                for cell in col:
                    self.assertTrue(cell.visited)
    
    def test_maze_reset_cells_visited(self):
        row_col_combos = [
            (10, 12),
            (29, 39),
            (40, 30)
        ]
        for (num_rows, num_cols) in row_col_combos:
            m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None, 0)
            m1._break_entrance_and_exit()
            m1._break_walls_r(0, 0)

            for col in m1._cells:
                for cell in col:
                    self.assertTrue(cell.visited)

            m1._reset_cells_visited()

            for col in m1._cells:
                for cell in col:
                    self.assertFalse(cell.visited)


if __name__ == "__main__":
    unittest.main()