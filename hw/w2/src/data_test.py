import unittest
from DATA import DATA
from ROW import ROW
from COLS import COLS

class TestDATA(unittest.TestCase):
    def test_init(self):
        data = DATA([])
        self.assertEqual(data.rows, [])
        self.assertIsNone(data.cols)

    def test_add_with_no_existing_cols(self):
        data = DATA([])
        test_row = ['a', 'b', 'c']
        data.add(test_row)
        self.assertIsNotNone(data.cols)
        self.assertEqual(len(data.rows), 1)
        self.assertIsInstance(data.rows[0], ROW)

    def test_add_with_existing_cols(self):
        data = DATA([])
        data.cols = COLS(ROW(['x', 'y', 'z']))  # Mocking COLS instance
        test_row = ['a', 'b', 'c']
        data.add(test_row)
        self.assertEqual(len(data.rows), 1)
        self.assertIsInstance(data.rows[0], ROW)

    # Add more test cases for mid, div, small, and stats methods
    # after implementing their logic in COLS and ROW classes.

if __name__ == '__main__':
    unittest.main()
