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
            print(f"Testing with {num_rows} rows and {num_cols} cols")
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
            print(f"Testing with {num_rows} rows and {num_cols} cols")
            m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
            self.assertEqual(
                len(m1._cells),
                num_cols,
            )
            self.assertEqual(
                len(m1._cells[0]),
                num_rows,
            )

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

if __name__ == "__main__":
    unittest.main()