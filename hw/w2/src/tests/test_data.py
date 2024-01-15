import unittest
from DATA import DATA
from ROW import ROW
from COLS import COLS

class TestDATA(unittest.TestCase):
    def test_init(self):
        data = DATA([])
        self.assertEqual(data.rows, [])
        self.assertIsNone(data.cols)

    def test_addition_of_rows(self):
        # Test addition of rows to DATA
        data = DATA([])
        data.cols = COLS(ROW(['Age', 'name', 'Grade!']))
        test_row = [12, 'Jay', 32]
        data.add(test_row)
        test_row2 = [6, 'Jay', 12]
        data.add(test_row2)
        self.assertEqual(len(data.rows), 2, "Should have 2 rows added")
        self.assertIsNotNone(data.cols, "Cols should be initialized")

    def test_add_with_existing_cols(self):
        data = DATA([])
        data.cols = COLS(ROW(['Age', 'name', 'Grade!']))  # Mocking COLS instance
        test_row = [12, 'Jay', 32]
        data.add(test_row)
        test_row2 = [6, 'Jay', 12]
        data.add(test_row2)
        test_row3 = [6, 'Mihir', 12]
        data.add(test_row3)
        # print()
        self.assertEqual(len(data.rows), 3)
        self.assertIsInstance(data.rows[0], ROW)

if __name__ == '__main__':
    unittest.main()
