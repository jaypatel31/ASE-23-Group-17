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


    def test_mid_div_small_stats_methods(self):
        # Prepare DATA instance with some rows
        data = DATA([])
        data.cols = COLS(ROW(['Age', 'name', 'Grade!']))  # Mocking COLS instance
        test_row = [12, 'Jay', 32]
        data.add(test_row)
        test_row2 = [6, 'Jay', 12]
        data.add(test_row2)
        test_row3 = [6, 'Mihir', 12]
        data.add(test_row3)

        # Test mid method
        mid_result = data.mid()
        
        # Assuming mid returns a ROW with midpoints of each column
        self.assertIsInstance(mid_result, ROW, "Mid should return a ROW object")


        # Test small method
        small_result = data.small()
        # Assuming small returns a ROW with smallest values of each column
        self.assertIsInstance(small_result, ROW, "Small should return a ROW object")

        # Test stats method
        stats_result = data.stats()
        # Assuming stats returns a dictionary with statistics
        self.assertIsInstance(stats_result, dict, "Stats should return a dictionary")
        self.assertIn('.N', stats_result, "Stats should include count of rows")
        self.assertEqual(stats_result['.N'], 3, "Count of rows in stats should be 3")

if __name__ == '__main__':
    unittest.main()
